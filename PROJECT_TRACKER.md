# 📊 Project Tracker - Phishing Detection Tool

**Status:** 🟡 IN PROGRESS  
**Progress:** 0%  
**Current Week:** Tuần 1

---

## 📅 Timeline Tổng Quan

| Tuần | Giai đoạn | Mốc deadline | Trạng thái |
|------|-----------|--------------|------------|
| 1 | Research & Setup | 05/04/2026 | 🔴 Chưa bắt đầu |
| 2 | Core Development (Phase 1) | 12/04/2026 | ⚪ Pending |
| 3 | Core Development (Phase 2) | 19/04/2026 | ⚪ Pending |
| 4 | Integration & Testing | 26/04/2026 | ⚪ Pending |
| 5 | Demo & Final Report | 03/05/2026 | ⚪ Pending |

---

## 🎯 Chi Tiết Theo Tuần

### 📌 TUẦN 1: Research & Setup (01/04 - 05/04)

**Mục tiêu:** Hiểu rõ bài toán, thu thập dataset, setup environment

#### Tasks:

- [ ] **1.1** Nghiên cứu phishing techniques hiện tại (2024-2025 trends)
  - Assigned: Member 1
  - Deadline: 02/04
  - Deliverable: Báo cáo research 5-10 trang

- [ ] **1.2** Thu thập & chuẩn bị Dataset
  - Phishing URL datasets (PhishTank, OpenPhish)
  - Legitimate URL datasets (Alexa Top Sites, CommonCrawl)
  - Email phishing datasets (Kaggle, UCI ML Repository)
  - Assigned: Member 2
  - Deadline: 03/04
  - Deliverable: Dataset folder với ít nhất 10k samples

- [ ] **1.3** Setup Development Environment
  - [ ] Python virtual environment
  - [ ] Git repository (init, .gitignore, branching strategy)
  - [ ] Docker setup
  - [ ] CI/CD pipeline (GitHub Actions)
  - Assigned: Member 3
  - Deadline: 03/04
  - Deliverable: Repo ready to code

- [ ] **1.4** Design Architecture
  - [ ] System architecture diagram
  - [ ] API specification (OpenAPI/Swagger)
  - [ ] Database schema
  - [ ] ML model selection strategy
  - Assigned: Member 4
  - Deadline: 05/04
  - Deliverable: docs/design.md

- [ ] **1.5** Weekly Standup Meeting
  - Schedule: 05/04/2026 (Saturday)
  - Nội dung: Review research, assign week 2 tasks

---

### 📌 TUẦN 2: Core Development Phase 1 (06/04 - 12/04)

**Mục tiêu:** Hoàn thành ML model training & evaluation

#### Tasks:

- [ ] **2.1** Feature Engineering - URL Features
  - Domain extraction & analysis
  - Path analysis (length, special chars, entropy)
  - URL structure features (subdomain, TLD, protocol)
  - Reputation features (Alexa rank, WHOIS data)
  - Assigned: Member 2
  - Deadline: 08/04

- [ ] **2.2** Feature Engineering - Email Features
  - Header analysis (From, Reply-To, SPF, DKIM, DMARC)
  - Body text analysis (suspicious keywords, urgency language)
  - Attachment detection
  - Link extraction from body
  - Assigned: Member 1
  - Deadline: 08/04

- [ ] **2.3** ML Model Training - URL Classifier
  - Algorithms: Random Forest, XGBoost, Neural Network
  - Training & validation pipeline
  - Hyperparameter tuning
  - Assigned: Member 2 + 4
  - Deadline: 10/04

- [ ] **2.4** ML Model Training - Email Classifier
  - NLP-based classification (TF-IDF + SVM, hoặc BERT-based)
  - Training & validation pipeline
  - Assigned: Member 1 + 4
  - Deadline: 10/04

- [ ] **2.5** Model Evaluation
  - Precision, Recall, F1-Score
  - Confusion matrix analysis
  - ROC/AUC curves
  - Cross-validation results
  - Assigned: All
  - Deadline: 12/04

- [ ] **2.6** Weekly Standup Meeting
  - Schedule: 12/04/2026 (Sunday)
  - Nội dung: Model review, integration plan

---

### 📌 TUẦN 3: Core Development Phase 2 (13/04 - 19/04)

**Mục tiêu:** Hoàn thành API, scraper, và frontend basics

#### Tasks:

- [ ] **3.1** Backend API Development
  - [ ] FastAPI setup
  - [ ] `/analyze/url` endpoint
  - [ ] `/analyze/email` endpoint
  - [ ] `/analyze/batch` endpoint
  - [ ] Authentication (JWT)
  - [ ] Rate limiting
  - Assigned: Member 3
  - Deadline: 15/04

- [ ] **3.2** Web Scraper Module
  - [ ] URL fetcher (fetch + parse HTML)
  - [ ] Screenshot capture (Selenium)
  - [ ] Visual similarity checker ( perceptual hash)
  - [ ] Brand detection
  - Assigned: Member 4
  - Deadline: 15/04

- [ ] **3.3** Email Parser Module
  - [ ] IMAP/POP3 connector
  - [ ] Email header parser
  - [ ] Body extraction (HTML + plain text)
  - [ ] Attachment sandboxing (basic)
  - Assigned: Member 1
  - Deadline: 15/04

- [ ] **3.4** Frontend Development - Phase 1
  - [ ] React setup (Vite)
  - [ ] Dashboard layout
  - [ ] URL analysis form + results display
  - [ ] Email analysis form + results display
  - Assigned: Member 3
  - Deadline: 18/04

- [ ] **3.5** Database Integration
  - [ ] PostgreSQL schema
  - [ ] Analysis history table
  - [ ] User feedback table (for active learning)
  - Assigned: Member 2 + 3
  - Deadline: 18/04

- [ ] **3.6** Weekly Standup Meeting
  - Schedule: 19/04/2026 (Sunday)
  - Nội dung: Integration check, bug fixes

---

### 📌 TUẦN 4: Integration & Testing (20/04 - 26/04)

**Mục tiêu:** Tích hợp toàn bộ, testing, bug fixes

#### Tasks:

- [ ] **4.1** System Integration
  - Connect frontend ↔ backend ↔ ML models
  - End-to-end testing workflow
  - Error handling & logging
  - Assigned: All
  - Deadline: 22/04

- [ ] **4.2** Unit Testing
  - Test coverage > 70%
  - Backend: pytest
  - Frontend: Jest / React Testing Library
  - ML: model validation tests
  - Assigned: Member 1 + 2
  - Deadline: 23/04

- [ ] **4.3** Security Testing
  - [ ] Input validation
  - [ ] SQL injection prevention
  - [ ] XSS prevention
  - [ ] Rate limiting verification
  - Assigned: Member 4
  - Deadline: 24/04

- [ ] **4.4** Performance Testing
  - Load testing (k8s/locust)
  - Model inference speed optimization
  - Database query optimization
  - Assigned: Member 2
  - Deadline: 24/04

- [ ] **4.5** Bug Fixes & Refinement
  - Priority: Critical → High → Medium
  - Code review
  - Documentation updates
  - Assigned: All
  - Deadline: 26/04

- [ ] **4.6** Weekly Standup Meeting
  - Schedule: 26/04/2026 (Sunday)
  - Nội dung: Final check before demo

---

### 📌 TUẦN 5: Demo & Final Report (27/04 - 03/05)

**Mục tiêu:** Hoàn thiện demo, báo cáo, presentation

#### Tasks:

- [ ] **5.1** Demo Video Recording
  - 5-10 phút demo
  - Voiceover explanation
  - Include: URL scan, email scan, dashboard
  - Assigned: Member 3
  - Deadline: 29/04

- [ ] **5.2** Final Report
  - [ ] Executive Summary
  - [ ] System Architecture
  - [ ] Implementation Details
  - [ ] ML Model Documentation
  - [ ] Evaluation Results
  - [ ] User Guide
  - [ ] Limitations & Future Work
  - Format: PDF (20-30 trang)
  - Assigned: Member 1
  - Deadline: 01/05

- [ ] **5.3** Presentation Slides
  - 15-20 slides
  - Team intro, problem statement, solution, demo, Q&A
  - Assigned: Member 2 + 4
  - Deadline: 01/05

- [ ] **5.4** Repository Cleanup
  - [ ] README.md final version
  - [ ] LICENSE
  - [ ] Demo deployment (Railway/Render/Heroku)
  - [ ] Clean commit history
  - Assigned: Member 3
  - Deadline: 02/05

- [ ] **5.5** Final Submission
  - Submit code + report + presentation
  - Deadline: 03/05/2026

---

## 👥 Task Assignment Summary

| Thành viên | Tuần 1 | Tuần 2 | Tuần 3 | Tuần 4 | Tuần 5 |
|------------|--------|--------|--------|--------|--------|
| **Member 1** | Research docs | Email features + ML | Email parser | Unit tests | Final Report |
| **Member 2** | Dataset | URL features + ML | Database | Performance | Slides support |
| **Member 3** | Dev Env Setup | API support | Backend API + Frontend | Integration | Demo video |
| **Member 4** | Architecture design | ML support | Web scraper | Security testing | Slides + Presentation |

---

## 📈 Progress Tracking

```
Week 1: [░░░░░░░░░░] 0%
Week 2: [░░░░░░░░░░] 0%
Week 3: [░░░░░░░░░░] 0%
Week 4: [░░░░░░░░░░] 0%
Week 5: [░░░░░░░░░░] 0%
```

---

## 🔗 Useful Resources

### Datasets
- PhishTank: https://www.phishtank.org/
- OpenPhish: https://openphish.com/
- Kaggle Phishing URL Dataset
- UCI ML Repository - Phishing Websites

### References
- OWASP Top 10
- Google Safe Browsing API
- VirusTotal API
- NLTK Documentation
- Scikit-learn Documentation

---

**Last Updated:** 01/04/2026
**Next Meeting:** 05/04/2026 (Weekly Standup)
