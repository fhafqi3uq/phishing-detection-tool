# 🏗️ System Architecture

## Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                        FRONTEND (React)                          │
│   Dashboard │ URL Input │ Email Input │ Results │ History        │
└───────────────────────────┬─────────────────────────────────────┘
                            │ HTTP/REST
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                     BACKEND (FastAPI)                            │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────────┐    │
│  │ URL API  │  │Email API │  │ Batch API│  │  Auth API    │    │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └──────┬───────┘    │
│       │             │             │                │            │
│       └─────────────┴─────────────┴────────────────┘            │
│                              │                                   │
│                    ┌─────────▼─────────┐                        │
│                    │   Analysis Core   │                        │
│                    │  (Feature Extract)│                        │
│                    └─────────┬─────────┘                        │
└──────────────────────────────┼──────────────────────────────────┘
                               │
          ┌────────────────────┼────────────────────┐
          │                    │                    │
          ▼                    ▼                    ▼
┌──────────────────┐ ┌──────────────────┐ ┌──────────────────────┐
│   ML ENGINE       │ │   SCRAPER        │ │   EMAIL PARSER       │
│  ┌─────────────┐  │ │  ┌───────────┐  │ │  ┌────────────────┐   │
│  │URL Classifier│  │ │  │URL Fetcher│  │ │  │IMAP/POP3      │   │
│  │(XGBoost/RF) │  │ │  │Screenshot │  │ │  │Header Parser  │   │
│  ├─────────────┤  │ │  │VisHash    │  │ │  │Body Extractor │   │
│  │Email Class. │  │ │  └───────────┘  │ │  │Link Extractor │   │
│  │(BERT/TF-IDF)│  │ │                 │ │  └────────────────┘   │
│  └─────────────┘  │ └──────────────────┘ └──────────────────────┘
└────────┬──────────┘
         │
         ▼
┌──────────────────┐
│   DATABASE       │
│  ┌────────────┐  │
│  │PostgreSQL  │  │
│  │History     │  │
│  │User Feedback│ │
│  └────────────┘  │
└──────────────────┘
```

---

## Component Details

### 1. Frontend (React + TailwindCSS)

**Responsibilities:**
- User input forms (URL, Email)
- Display analysis results
- History visualization
- Real-time notifications

**API Endpoints consumed:**
- `POST /api/v1/analyze/url`
- `POST /api/v1/analyze/email`
- `GET /api/v1/history`
- `POST /api/v1/feedback`

---

### 2. Backend (FastAPI)

**Responsibilities:**
- REST API routing
- Request validation
- Authentication (JWT)
- Rate limiting
- Response formatting

**Endpoints:**

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/analyze/url` | Analyze single URL |
| POST | `/api/v1/analyze/email` | Analyze email content/headers |
| POST | `/api/v1/analyze/batch` | Batch analyze URLs |
| GET | `/api/v1/history` | Get analysis history |
| GET | `/api/v1/stats` | Get detection statistics |
| POST | `/api/v1/feedback` | Submit user feedback |

---

### 3. ML Engine

#### 3.1 URL Classifier

**Features extracted:**
```
- url_length
- num_dots
- num_hyphens
- num_underscores
- num_slashes
- num_special_chars
- has_https
- domain_length
- subdomain_count
- path_length
- query_length
- entropy (character)
- alexa_rank
- whois_age_days
- tld_category
- suspicious_keywords_count
- ip_address_in_url
- url_shortener_detected
```

**Models to try:**
1. XGBoost (baseline)
2. Random Forest
3. Gradient Boosting
4. Neural Network (MLP)

**Best model:** XGBoost with ~95% accuracy target

#### 3.2 Email Classifier

**Features extracted:**
```
- header_authentication (SPF, DKIM, DMARC status)
- sender_domain_reputation
- reply_to_mismatch
- subject_urgency_score
- body_urgency_score
- suspicious_keywords_count
- link_count
- external_link_count
- attachment_present
- html_ratio
- sender_name_spoofing_detected
```

**Models to try:**
1. TF-IDF + SVM (baseline)
2. BERT-based classifier
3. RoBERTa fine-tuned

**Best model:** BERT-based with ~93% accuracy target

---

### 4. Web Scraper Module

**Capabilities:**
- Fetch URL content (HEAD + GET)
- Parse HTML for links
- Screenshot capture (headless Chrome)
- Perceptual hash (pHash) for visual similarity
- Brand detection via logo analysis

**Brands to detect:**
- Google, Facebook, Microsoft, Apple, Amazon, PayPal, Banks ( Vietcombank, VietinBank, BIDV...)

---

### 5. Email Parser Module

**Capabilities:**
- IMAP/POP3 connection
- Header parsing (From, Reply-To, Return-Path, Received)
- SPF/DKIM/DMARC validation
- Body extraction (HTML + plain text)
- Link extraction
- Attachment detection

---

### 6. Database Schema

```sql
-- Analysis history
CREATE TABLE analysis_results (
    id SERIAL PRIMARY KEY,
    input_type VARCHAR(10), -- 'url' or 'email'
    input_content TEXT,
    result_label VARCHAR(20), -- 'phishing' or 'legitimate'
    confidence_score FLOAT,
    features_used JSONB,
    processed_at TIMESTAMP DEFAULT NOW(),
    user_id INTEGER REFERENCES users(id)
);

-- User feedback (for active learning)
CREATE TABLE user_feedback (
    id SERIAL PRIMARY KEY,
    analysis_id INTEGER REFERENCES analysis_results(id),
    user_verdict VARCHAR(20),
    created_at TIMESTAMP DEFAULT NOW()
);

-- Users table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE,
    password_hash VARCHAR(255),
    created_at TIMESTAMP DEFAULT NOW()
);
```

---

## Data Flow

### URL Analysis Flow

```
User Input URL
      │
      ▼
┌─────────────┐
│  Validation │ ← Basic URL format check
└──────┬──────┘
       │
       ▼
┌─────────────┐     ┌─────────────┐
│   Scraper   │────►│  Screenshot │ (optional)
│   Module    │     │   Capture   │
└──────┬──────┘     └─────────────┘
       │
       ▼
┌─────────────┐
│  Feature    │
│  Extraction │ ← URL features + Visual features
└──────┬──────┘
       │
       ▼
┌─────────────┐
│    ML       │
│   Engine    │ ───► URL Classifier
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Result    │ → Phishing/Legitimate + Confidence
│  Generator  │
└─────────────┘
```

### Email Analysis Flow

```
User Input Email
      │
      ▼
┌─────────────┐
│    Email    │ ← Raw email (MIME format)
│    Parser   │
└──────┬──────┘
       │
       ├──────► Header Analysis ──► SPF/DKIM/DMARC check
       │
       ▼
┌─────────────┐
│  Feature    │
│  Extraction │ ← Text features + Header features
└──────┬──────┘
       │
       ▼
┌─────────────┐
│    ML       │
│   Engine    │ ───► Email Classifier
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Result    │ → Phishing/Legitimate + Confidence
│  Generator  │
└─────────────┘
```

---

## Deployment Architecture

```
                    ┌─────────────────┐
                    │   Cloudflare   │
                    │   (CDN + WAF)  │
                    └────────┬───────┘
                             │
                    ┌────────▼───────┐
                    │  Load Balancer  │
                    └────────┬───────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
┌───────▼───────┐    ┌───────▼───────┐    ┌───────▼───────┐
│  Frontend Pod  │    │  Backend Pod   │    │  Backend Pod   │
│   (React)      │    │  (FastAPI)     │    │  (FastAPI)     │
└────────────────┘    └───────┬───────┘    └───────┬───────┘
                              │                    │
                    ┌─────────┴─────────┐
                    │                    │
             ┌──────▼───────┐    ┌──────▼───────┐
             │  ML Service   │    │  PostgreSQL   │
             │  (GPU Pod)    │    │  (RDS)        │
             └───────────────┘    └───────────────┘
```

**Platform options:**
- Railway (easy deploy)
- Render
- Google Cloud Run
- AWS ECS/Fargate

---

## Security Considerations

1. **Input Validation** - Sanitize all user inputs
2. **Rate Limiting** - Prevent abuse (100 req/min per user)
3. **SSRF Prevention** - Block internal IP ranges in URL fetches
4. **Authentication** - JWT with refresh tokens
5. **Data Encryption** - TLS in transit, encrypted at rest
6. **Sandboxing** - Email attachments analyzed in isolation

---

## Performance Targets

| Metric | Target |
|--------|--------|
| URL Analysis Latency | < 2 seconds |
| Email Analysis Latency | < 5 seconds |
| Batch Analysis (100 URLs) | < 30 seconds |
| API Availability | 99.9% |
| Model Accuracy | > 93% |
| Model F1 Score | > 92% |
