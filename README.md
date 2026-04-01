# 🎣 Phishing Detection Tool

**Đề tài:** Phát hiện email/website lừa đảo sử dụng Machine Learning & NLP

**Thành viên:** 4 người  
**Thời gian:** 5 tuần  
**Ngày bắt đầu:** 01/04/2026

---

## Mục tiêu

Xây dựng tool phát hiện phishing dựa trên:
- URL features (domain, path, length, special chars...)
- Email content analysis (sender, subject, body)
- NLP-based content classification
- Visual similarity với legitimate sites

---

## Tech Stack

| Layer | Tech |
|-------|------|
| Language | Python 3.10+ |
| ML/NLP | Scikit-learn, NLTK/Transformers |
| Web Scraping | BeautifulSoup, Selenium |
| API | Flask/FastAPI |
| Frontend | React + TailwindCSS |
| Database | PostgreSQL |
| Deployment | Docker |

---

## Repository Structure

```
phishing-detection-tool/
├── docs/           # Tài liệu thiết kế
├── src/            # Source code
│   ├── backend/    # Flask/FastAPI
│   ├── ml/         # ML models
│   └── scraper/    # Web/Email scraper
├── data/           # Datasets + trained models
├── tests/          # Unit tests
└── reports/        # Báo cáo + presentation
```
