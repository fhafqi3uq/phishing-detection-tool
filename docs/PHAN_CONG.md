# 📋 PHÂN CÔNG CÔNG VIỆC

**Đề tài:** Phishing Detection Tool  
**Trưởng nhóm:** Quang  
**Thành viên:** 4 người  
**Deadline tuần 1:** 05/04/2026

---

## 👥 PHÂN CÔNG CHI TIẾT

| Người | Phần việc | File output | Deadline |
|-------|-----------|-------------|----------|
| **Quang (Trưởng nhóm)** | Setup repo + Phân công + Theo dõi | - | Hàng ngày |
| **Member 1** | Research phishing 2024-2025 | `docs/research.md` | 02/04 |
| **Member 2** | Thu thập Dataset (PhishTank, Kaggle) | `data/raw/` | 03/04 |
| **Member 3** | Setup Dev Environment (Python venv) | `requirements.txt`, `venv/` | 03/04 |
| **Member 4** | Thiết kế System Architecture | `docs/ARCHITECTURE.md` | 05/04 |

---

## 📝 CHI TIẾT TỪNG PHẦN VIỆC

### 👤 MEMBER 1: RESEARCH
```
Nhiệm vụ: Nghiên cứu và viết báo cáo về phishing

Nội dung cần viết (5-10 trang):
1. Tổng quan về phishing (định nghĩa, thống kê 2024-2025)
2. Các loại phishing phổ biến
   - Email phishing
   - Website phishing (URL)
   - Spear phishing
   - Whaling
3. Indicators nhận biết phishing
   - URL suspicious patterns
   - Email header analysis
   - Content patterns
4. Case studies nổi tiếng
5. Cách phòng chống

Output: docs/research.md (Markdown hoặc Google Docs)
Deadline: 02/04/2026
```

### 👤 MEMBER 2: DATASET
```
Nhiệm vụ: Thu thập dataset cho ML training

Cần thu thập:
1. Phishing URLs (label = 1)
   - PhishTank: https://www.phishtank.org/
   - OpenPhish: https://openphish.com/
   - Kaggle: https://www.kaggle.com/datasets/akashkr/phishing-website-dataset

2. Legitimate URLs (label = 0)
   - Alexa Top 1 Million: https://www.alexa.com/topsites
   - CommonCrawl

3. Email datasets (nếu có)
   - Kaggle Phishing Email dataset

Output: 
- data/raw/phishing_urls.csv
- data/raw/legitimate_urls.csv
- data/raw/emails.csv

Format: CSV với cột url, label (1=phishing, 0=legit)
Deadline: 03/04/2026
```

### 👤 MEMBER 3: DEV ENVIRONMENT
```
Nhiệm vụ: Setup môi trường phát triển

Các bước:
1. Tạo Python virtual environment
   python -m venv venv
   
2. Cài đặt packages cần thiết:
   pip install fastapi uvicorn scikit-learn xgboost beautifulsoup4 selenium nltk pandas numpy

3. Tạo requirements.txt:
   pip freeze > requirements.txt

4. (Tuỳ chọn) Tạo Dockerfile

5. Test xem có chạy được không:
   python -c "import fastapi; print('OK')"

Output:
- requirements.txt
- venv/ (không push lên git, thêm vào .gitignore)
- Dockerfile (bonus)

Deadline: 03/04/2026
```

### 👤 MEMBER 4: ARCHITECTURE
```
Nhiệm vụ: Thiết kế kiến trúc hệ thống

Cần vẽ/viết:
1. System Architecture Diagram
   - Frontend (React)
   - Backend (FastAPI)
   - ML Engine
   - Database
   
2. API Endpoints Specification:
   - POST /api/v1/analyze/url
   - POST /api/v1/analyze/email
   - GET /api/v1/history
   - POST /api/v1/feedback
   
3. Database Schema:
   - users table
   - analysis_results table
   - user_feedback table

4. Data Flow:
   - URL analysis flow
   - Email analysis flow

Output: docs/ARCHITECTURE.md (có hình vẽ - dùng draw.io hoặc Excalidraw)
Deadline: 05/04/2026
```

---

## 📊 THEO DÕI TIẾN ĐỘ

### Tuần 1: Research & Setup (01/04 - 05/04)

| Task | Assigned | Deadline | Status | Notes |
|------|----------|----------|--------|-------|
| 1.1 Setup GitHub repo | Quang | 01/04 | ✅ DONE | |
| 1.2 Research phishing | Member 1 | 02/04 | ⬜ TODO | |
| 1.3 Thu thập Dataset | Member 2 | 03/04 | ⬜ TODO | |
| 1.4 Setup Env | Member 3 | 03/04 | ⬜ TODO | |
| 1.5 Architecture | Member 4 | 05/04 | ⬜ TODO | |
| 1.6 Họp nhóm | All | 05/04 | ⬜ TODO | |

### Tuần 2: ML Development Phase 1 (06/04 - 12/04)

| Task | Assigned | Deadline | Status | Notes |
|------|----------|----------|--------|-------|
| 2.1 URL Feature Extraction | Member 2 | 08/04 | ⬜ TODO | |
| 2.2 Email Feature Extraction | Member 1 | 08/04 | ⬜ TODO | |
| 2.3 Train URL Model | Member 2+4 | 10/04 | ⬜ TODO | |
| 2.4 Train Email Model | Member 1+4 | 10/04 | ⬜ TODO | |
| 2.5 Model Evaluation | All | 12/04 | ⬜ TODO | |

### Tuần 3: ML Development Phase 2 (13/04 - 19/04)

| Task | Assigned | Deadline | Status | Notes |
|------|----------|----------|--------|-------|
| 3.1 Backend API | Member 3 | 15/04 | ⬜ TODO | |
| 3.2 Web Scraper | Member 4 | 15/04 | ⬜ TODO | |
| 3.3 Email Parser | Member 1 | 15/04 | ⬜ TODO | |
| 3.4 Frontend Basic | Member 3 | 18/04 | ⬜ TODO | |

### Tuần 4: Integration & Testing (20/04 - 26/04)

| Task | Assigned | Deadline | Status | Notes |
|------|----------|----------|--------|-------|
| 4.1 System Integration | All | 22/04 | ⬜ TODO | |
| 4.2 Unit Testing | Member 1+2 | 23/04 | ⬜ TODO | |
| 4.3 Security Testing | Member 4 | 24/04 | ⬜ TODO | |
| 4.4 Bug Fixes | All | 26/04 | ⬜ TODO | |

### Tuần 5: Demo & Report (27/04 - 03/05)

| Task | Assigned | Deadline | Status | Notes |
|------|----------|----------|--------|-------|
| 5.1 Demo Video | Member 3 | 29/04 | ⬜ TODO | |
| 5.2 Final Report | Member 1 | 01/05 | ⬜ TODO | |
| 5.3 Presentation | Member 2+4 | 01/05 | ⬜ TODO | |
| 5.4 Submit | All | 03/05 | ⬜ TODO | |

---

## 📅 LỊCH HỌP

| Lần | Ngày | Nội dung |
|-----|------|----------|
| 1 | 05/04/2026 | Review tuần 1, confirm architecture |
| 2 | 12/04/2026 | Review ML models |
| 3 | 19/04/2026 | Review API + Frontend |
| 4 | 26/04/2026 | Final check trước demo |
| 5 | 03/05/2026 | Họp final + submit |

---

## 🔗 LIÊN KẾT

- **GitHub Repo:** https://github.com/quocquang2610/phishing-detection-tool
- **Google Docs (Research):** [Chia sẻ link sau]
- **Google Sheets (Progress):** [Chia sẻ link sau]

---

## 📱 LIÊN LẠC

| Thành viên | Email | Zalo/Messenger | Phần việc |
|------------|-------|----------------|-----------|
| Quang | | | Trưởng nhóm |
| Member 1 | | | Research |
| Member 2 | | | Dataset |
| Member 3 | | | Dev Env |
| Member 4 | | | Architecture |

---

**Cập nhật lần cuối:** 01/04/2026
**Trưởng nhóm cập nhật:** Quang
