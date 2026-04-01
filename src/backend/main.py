"""
Phishing Detection Tool - Main API Entry Point
FastAPI backend for URL and Email phishing detection
"""

from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel, HttpUrl
from typing import Optional, List
from datetime import datetime
import joblib
import os

# ============== APP SETUP ==============

app = FastAPI(
    title="Phishing Detection API",
    description="ML-powered phishing detection for URLs and Emails",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure properly in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Security
security = HTTPBearer(auto_error=False)

# ============== MODELS ==============

class URLAnalysisRequest(BaseModel):
    url: str
    include_screenshot: bool = False

class EmailAnalysisRequest(BaseModel):
    subject: Optional[str] = None
    body: str
    headers: Optional[dict] = None

class BatchURLRequest(BaseModel):
    urls: List[str]

class AnalysisResponse(BaseModel):
    input_type: str
    input_content: str
    result_label: str  # "phishing" or "legitimate"
    confidence_score: float
    risk_level: str  # "high", "medium", "low"
    features: dict
    analyzed_at: datetime

class BatchAnalysisResponse(BaseModel):
    total: int
    phishing_count: int
    legitimate_count: int
    results: List[AnalysisResponse]

# ============== ML MODEL LOADING ==============

# Lazy loading - models loaded on first use
_url_model = None
_email_model = None

def get_url_model():
    global _url_model
    if _url_model is None:
        model_path = os.path.join(os.path.dirname(__file__), "ml", "models", "url_classifier.pkl")
        if os.path.exists(model_path):
            _url_model = joblib.load(model_path)
        else:
            _url_model = None  # Placeholder
    return _url_model

def get_email_model():
    global _email_model
    if _email_model is None:
        model_path = os.path.join(os.path.dirname(__file__), "ml", "models", "email_classifier.pkl")
        if os.path.exists(model_path):
            _email_model = joblib.load(model_path)
        else:
            _email_model = None  # Placeholder
    return _email_model

# ============== FEATURE EXTRACTION ==============

def extract_url_features(url: str) -> dict:
    """Extract features from URL for ML model"""
    from urllib.parse import urlparse
    import re
    import math
    
    parsed = urlparse(url)
    domain = parsed.netloc
    path = parsed.path
    query = parsed.query
    
    # Basic features
    features = {
        "url_length": len(url),
        "domain_length": len(domain),
        "path_length": len(path),
        "query_length": len(query),
        "num_dots": url.count('.'),
        "num_hyphens": url.count('-'),
        "num_underscores": url.count('_'),
        "num_slashes": url.count('/'),
        "num_special_chars": len(re.findall(r'[^a-zA-Z0-9]', url)),
        "has_https": 1 if parsed.scheme == "https" else 0,
        "has_ip": 1 if re.match(r'\d+\.\d+\.\d+\.\d+', domain) else 0,
        "subdomain_count": domain.count('.') - 1 if domain.count('.') > 1 else 0,
        "entropy": calculate_entropy(url),
        "suspicious_keywords": sum([
            url.count(kw) for kw in [
                'login', 'signin', 'verify', 'account', 'update',
                'secure', 'banking', 'confirm', 'password', 'credential'
            ]
        ]),
        "url_shortener": 1 if any(shortener in url for shortener in [
            'bit.ly', 'tinyurl', 'goo.gl', 't.co', 'ow.ly'
        ]) else 0,
    }
    
    return features

def calculate_entropy(text: str) -> float:
    """Calculate Shannon entropy of string"""
    import math
    from collections import Counter
    
    if not text:
        return 0
    
    prob = [float(count) / len(text) for count in Counter(text).values()]
    entropy = -sum(p * math.log2(p) for p in prob if p > 0)
    return entropy

def extract_email_features(subject: str, body: str, headers: dict) -> dict:
    """Extract features from email content"""
    import re
    
    features = {}
    
    # Subject features
    features['subject_length'] = len(subject) if subject else 0
    features['subject_urgency_score'] = sum([
        1 if kw in subject.lower() else 0 
        for kw in ['urgent', 'immediately', 'action required', 'suspended', 'verify']
    ]) if subject else 0
    
    # Body features
    features['body_length'] = len(body)
    features['urgency_score'] = sum([
        1 if kw in body.lower() else 0 
        for kw in [
            'urgent', 'immediately', 'action required', 'suspended',
            'verify your', 'confirm your', 'update your', 'click here',
            'act now', 'limited time', 'deadline'
        ]
    ])
    
    # Link features
    links = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', body)
    features['link_count'] = len(links)
    features['external_link_count'] = len(links)
    
    # Suspicious patterns
    features['has_password_request'] = 1 if 'password' in body.lower() else 0
    features['has_credit_card_request'] = 1 if any(kw in body.lower() for kw in ['credit card', 'card number', 'cvv']) else 0
    features['has_login_link'] = 1 if any(kw in body.lower() for kw in ['login', 'sign in', 'log in']) else 0
    
    # Header features (if provided)
    if headers:
        features['has_spf'] = 1 if headers.get('spf', '').lower() == 'pass' else 0
        features['has_dkim'] = 1 if headers.get('dkim', '').lower() == 'pass' else 0
        features['has_dmarc'] = 1 if headers.get('dmarc', '').lower() == 'pass' else 0
    else:
        features['has_spf'] = 0
        features['has_dkim'] = 0
        features['has_dmarc'] = 0
    
    return features

# ============== PREDICTION HELPERS ==============

def predict_url(url: str, features: dict) -> dict:
    """Make prediction on URL"""
    model = get_url_model()
    
    if model is None:
        # Placeholder logic until model is trained
        # Simple rule-based fallback
        suspicious_count = features.get('suspicious_keywords', 0)
        entropy = features.get('entropy', 0)
        
        if suspicious_count >= 3 or entropy > 4.5 or features.get('has_ip', 0):
            return {
                "result_label": "phishing",
                "confidence_score": 0.75,
                "risk_level": "high"
            }
        else:
            return {
                "result_label": "legitimate",
                "confidence_score": 0.80,
                "risk_level": "low"
            }
    
    # Real model prediction would go here
    # feature_vector = ...  # Convert dict to array
    # prediction = model.predict(feature_vector)
    # probability = model.predict_proba(feature_vector)
    
    return {"result_label": "pending", "confidence_score": 0, "risk_level": "unknown"}

def predict_email(subject: str, body: str, features: dict) -> dict:
    """Make prediction on email"""
    model = get_email_model()
    
    if model is None:
        # Placeholder
        urgency = features.get('urgency_score', 0)
        has_password_request = features.get('has_password_request', 0)
        
        if urgency >= 3 or has_password_request:
            return {
                "result_label": "phishing",
                "confidence_score": 0.70,
                "risk_level": "high"
            }
        else:
            return {
                "result_label": "legitimate",
                "confidence_score": 0.75,
                "risk_level": "low"
            }
    
    return {"result_label": "pending", "confidence_score": 0, "risk_level": "unknown"}

# ============== API ENDPOINTS ==============

@app.get("/")
async def root():
    return {"message": "Phishing Detection API", "version": "1.0.0"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "models_loaded": get_url_model() is not None}

@app.post("/api/v1/analyze/url", response_model=AnalysisResponse)
async def analyze_url(request: URLAnalysisRequest):
    """Analyze a single URL for phishing indicators"""
    try:
        # Extract features
        features = extract_url_features(request.url)
        
        # Make prediction
        prediction = predict_url(request.url, features)
        
        return AnalysisResponse(
            input_type="url",
            input_content=request.url,
            result_label=prediction["result_label"],
            confidence_score=prediction["confidence_score"],
            risk_level=prediction["risk_level"],
            features=features,
            analyzed_at=datetime.now()
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/v1/analyze/email", response_model=AnalysisResponse)
async def analyze_email(request: EmailAnalysisRequest):
    """Analyze email content for phishing indicators"""
    try:
        # Extract features
        features = extract_email_features(
            request.subject or "",
            request.body,
            request.headers or {}
        )
        
        # Make prediction
        prediction = predict_email(request.subject or "", request.body, features)
        
        return AnalysisResponse(
            input_type="email",
            input_content=request.subject or "(no subject)",
            result_label=prediction["result_label"],
            confidence_score=prediction["confidence_score"],
            risk_level=prediction["risk_level"],
            features=features,
            analyzed_at=datetime.now()
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/v1/analyze/batch", response_model=BatchAnalysisResponse)
async def analyze_batch(request: BatchURLRequest):
    """Analyze multiple URLs in batch"""
    results = []
    phishing_count = 0
    legitimate_count = 0
    
    for url in request.urls:
        features = extract_url_features(url)
        prediction = predict_url(url, features)
        
        if prediction["result_label"] == "phishing":
            phishing_count += 1
        else:
            legitimate_count += 1
        
        results.append(AnalysisResponse(
            input_type="url",
            input_content=url,
            result_label=prediction["result_label"],
            confidence_score=prediction["confidence_score"],
            risk_level=prediction["risk_level"],
            features=features,
            analyzed_at=datetime.now()
        ))
    
    return BatchAnalysisResponse(
        total=len(results),
        phishing_count=phishing_count,
        legitimate_count=legitimate_count,
        results=results
    )

# ============== RUN ==============

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
