# ĐỀ XUẤT ĐỀ TÀI

---

## I. THÔNG TIN ĐỀ TÀI

**1. Thông tin sinh viên**

| Thông tin | Chi tiết |
|-----------|----------|
| Họ và tên | Hồ Nguyễn Quốc Quang, Lê Duy Trung, Trần Trung Vỹ, Trương Đình Quân |
| Chuyên ngành | An ninh mạng (Cybersecurity) |
| Lớp | CS397B |
| Khoa | Kỹ thuật mạng và truyền thông |
| Ngày nộp | 01/04/2026 |

---

**2. Tên đề tài (ý tưởng/sản phẩm)**

> **Phishing Detection Tool - Hệ thống phát hiện lừa đảo trực tuyến**

---

## II. TỔNG QUAN (YÊU TƯỞNG)

Phishing (lừa đảo trực tuyến) là một trong những hình thức tấn công mạng phổ biến nhất hiện nay, chiếm hơn **90% các cuộc tấn công mạng** trên toàn thế giới. Đề tài này xây dựng một công cụ sử dụng **Machine Learning** và **NLP** để tự động phát hiện các email và website lừa đảo (phishing) dựa trên:

- Đặc điểm URL (độ dài, entropy, từ khóa đáng nghi, domain...)
- Nội dung email (header, body, link, file đính kèm)
- Đối sánh hình ảnh (visual similarity với các trang chính hãng)

---

## III. MỤC TIÊU

### Mục tiêu chính:
1. Xây dựng hệ thống phát hiện URL phishing với độ chính xác ≥ 93%
2. Xây dựng hệ thống phát hiện email phishing với độ chính xác ≥ 90%
3. Cung cấp API để tích hợp vào các hệ thống khác

### Mục tiêu phụ:
- Tạo giao diện dashboard để người dùng thông thường sử dụng
- Hỗ trợ quét hàng loạt (batch scan)
- Lưu trữ lịch sử phân tích

---

## IV. NGÔN NGỮ LẬP TRÌNH & CÔNG CỤ SỬ DỤNG

| Loại | Công nghệ |
|------|-----------|
| **Ngôn ngữ chính** | Python 3.10+ |
| **Backend API** | FastAPI |
| **Machine Learning** | Scikit-learn, XGBoost, NLTK |
| **Web Scraping** | BeautifulSoup, Selenium |
| **Database** | PostgreSQL |
| **Frontend** | React + TailwindCSS |
| **Container** | Docker |
| **Deployment** | Railway / Render |

### Thư viện ML/NLP:
- `scikit-learn` - ML framework
- `xgboost` - Gradient boosting
- `nltk` - NLP processing
- `beautifulsoup4` - HTML parsing
- `selenium` - Browser automation

---

## V. NỘI DUNG CÔNG VIỆC CẦN THỰC HIỆN

### Tuần 1: Research & Setup
- [ ] Nghiên cứu các kỹ thuật phishing mới nhất (2024-2025)
- [ ] Thu thập dataset (PhishTank, Kaggle, Alexa Top Sites)
- [ ] Setup development environment
- [ ] Thiết kế system architecture

### Tuần 2: ML Development Phase 1
- [ ] Trích xuất đặc trưng URL (30+ features)
- [ ] Trích xuất đặc trưng Email (header, body, links)
- [ ] Train URL classifier (XGBoost, Random Forest)
- [ ] Train Email classifier (TF-IDF + SVM/BERT)

### Tuần 3: ML Development Phase 2
- [ ] Phát triển Backend API (FastAPI)
- [ ] Phát triển Web Scraper module
- [ ] Phát triển Email Parser module
- [ ] Phát triển Frontend cơ bản

### Tuần 4: Integration & Testing
- [ ] Tích hợp toàn bộ hệ thống
- [ ] Unit testing (>70% coverage)
- [ ] Security testing
- [ ] Performance testing

### Tuần 5: Demo & Report
- [ ] Quay demo video
- [ ] Viết báo cáo final
- [ ] Làm slide thuyết trình
- [ ] Submit

---

## VI. ĐÁNH GIÁ CƠ SỞ KIẾN THỨC CỦA SINH VIÊN

| Thành viên | Kiến thức nền | Đánh giá |
|------------|---------------|-----------|
| Hồ Nguyễn Quốc Quang | [VD: Python, Networking, Security+] | Có nền tảng về security |
| Trương Đình Quân| [VD: ML/Data Science, Python] | Đã học Machine Learning |
| Lê Duy Trung | [VD: Web Development, API, React] | Có kinh nghiệm Frontend |
| Trần Trung Vỹ | [VD: Python, DevOps, Docker] | Biết về deployment |

**Đánh giá chung:** Nhóm có đủ kiến thức nền tảng về Python, ML, Web Development và Security để thực hiện đề tài.

---

## VII. ĐÁNH GIÁ KHẢ NĂNG PHÁT TRIỂN SẢN PHẨM

### Điểm mạnh:
- ✅ Sử dụng công nghệ ML/NLP tiên tiến, phù hợp xu hướng
- ✅ Dataset phong phú, dễ thu thập
- ✅ Ứng dụng thực tế cao (doanh nghiệp, cá nhân đều cần)
- ✅ Có thể mở rộng thành sản phẩm thương mại

### Điểm hạn chế & cách khắc phục:
- ⚠️ Phishing techniques liên tục thay đổi → Cần cập nhật model định kỳ
- ⚠️ False positive có thể xảy ra → Thêm lớp human review
- ⚠️ Performance khi xử lý batch lớn → Sử dụng caching + async processing

### Khả năng mở rộng:
- Tích hợp vào email server (Gmail, Outlook plugin)
- Xây dựng browser extension
- Phát triển thành SaaS product
- Thêm NLP model cho multi-language support

---

## VIII. GHI CHÚ

- Thời gian thực hiện: **5 tuần** (01/04/2026 - 03/05/2026)
- Số lượng thành viên: **4 người**
- Đề tài thuộc nhóm: **An toàn thông tin / Cybersecurity**
- Có thể liên hệ thực tế với các doanh nghiệp để test sản phẩm

---

**Ngày nộp:** 01/04/2026

