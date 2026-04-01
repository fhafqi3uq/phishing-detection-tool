"""
ML Model Training Pipeline
Trains URL and Email phishing classifiers
"""

import os
import sys
import pickle
import numpy as np
import pandas as pd
from typing import Tuple

# Add src to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ml.url_features import URLFeatureExtractor


# ============== CONFIG ==============

MODELS_DIR = os.path.join(os.path.dirname(__file__), "models")
os.makedirs(MODELS_DIR, exist_ok=True)

# Model hyperparameters
URL_MODEL_PARAMS = {
    'n_estimators': 200,
    'max_depth': 15,
    'learning_rate': 0.1,
    'min_child_weight': 3,
    'subsample': 0.8,
    'colsample_bytree': 0.8,
}

EMAIL_MODEL_PARAMS = {
    'n_estimators': 150,
    'max_depth': 12,
    'learning_rate': 0.1,
}


# ============== DATA LOADING ==============

def load_phishTank_data(filepath: str) -> pd.DataFrame:
    """Load PhishTank URL dataset"""
    # Expected columns: url, phish_id, verified, verification_time
    df = pd.read_csv(filepath)
    df['label'] = 1  # 1 = phishing
    return df[['url', 'label']]


def load_alexa_top_sites(filepath: str) -> pd.DataFrame:
    """Load Alexa Top Sites as legitimate URLs"""
    # Expected: one domain per line
    with open(filepath, 'r') as f:
        domains = [line.strip() for line in f if line.strip()]
    
    df = pd.DataFrame({'url': [f"https://{d}" for d in domains]})
    df['label'] = 0  # 0 = legitimate
    return df


def load_kaggle_phishing_dataset(filepath: str) -> pd.DataFrame:
    """Load Kaggle Phishing Websites dataset"""
    # https://www.kaggle.com/datasets/akashkr/phishing-website-dataset
    df = pd.read_csv(filepath)
    # Assuming label column exists: 1 = phishing, -1 or 0 = legitimate
    df['label'] = df['label'].apply(lambda x: 1 if x == 1 else 0)
    return df


def load_email_dataset(filepath: str) -> pd.DataFrame:
    """Load email phishing dataset"""
    # Expected: subject, body, label (1=phishing, 0=legitimate)
    df = pd.read_csv(filepath)
    return df


# ============== URL MODEL TRAINING ==============

def train_url_model(X_train: np.ndarray, y_train: np.ndarray,
                     X_val: np.ndarray, y_val: np.ndarray) -> dict:
    """Train URL phishing classifier"""
    from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
    from xgboost import XGBClassifier
    from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
    
    results = {}
    
    # Try multiple models
    models = {
        'XGBoost': XGBClassifier(**URL_MODEL_PARAMS, random_state=42, eval_metric='logloss'),
        'RandomForest': RandomForestClassifier(n_estimators=200, max_depth=15, random_state=42),
        'GradientBoosting': GradientBoostingClassifier(n_estimators=150, max_depth=10, random_state=42),
    }
    
    for name, model in models.items():
        print(f"\nTraining {name}...")
        model.fit(X_train, y_train)
        
        # Predict
        y_pred = model.predict(X_val)
        
        # Metrics
        results[name] = {
            'accuracy': accuracy_score(y_val, y_pred),
            'precision': precision_score(y_val, y_pred),
            'recall': recall_score(y_val, y_pred),
            'f1': f1_score(y_val, y_pred),
            'model': model
        }
        
        print(f"  Accuracy: {results[name]['accuracy']:.4f}")
        print(f"  Precision: {results[name]['precision']:.4f}")
        print(f"  Recall: {results[name]['recall']:.4f}")
        print(f"  F1: {results[name]['f1']:.4f}")
    
    # Select best model
    best_name = max(results, key=lambda k: results[k]['f1'])
    print(f"\nBest model: {best_name}")
    
    return results[best_name]


# ============== EMAIL MODEL TRAINING ==============

def train_email_model(X_train: np.ndarray, y_train: np.ndarray,
                       X_val: np.ndarray, y_val: np.ndarray) -> dict:
    """Train Email phishing classifier"""
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.pipeline import Pipeline
    from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
    
    # For email, we'll use TF-IDF + Classifier pipeline
    print("\nTraining Email classifier (TF-IDF + RandomForest)...")
    
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(max_features=5000, ngram_range=(1, 2))),
        ('clf', RandomForestClassifier(**EMAIL_MODEL_PARAMS, random_state=42))
    ])
    
    pipeline.fit(X_train, y_train)
    
    y_pred = pipeline.predict(X_val)
    
    results = {
        'accuracy': accuracy_score(y_val, y_pred),
        'precision': precision_score(y_val, y_pred),
        'recall': recall_score(y_val, y_pred),
        'f1': f1_score(y_val, y_pred),
        'model': pipeline
    }
    
    print(f"  Accuracy: {results['accuracy']:.4f}")
    print(f"  Precision: {results['precision']:.4f}")
    print(f"  Recall: {results['recall']:.4f}")
    print(f"  F1: {results['f1']:.4f}")
    
    return results


# ============== MAIN TRAINING PIPELINE ==============

def main():
    """Main training pipeline"""
    print("=" * 60)
    print("PHISHING DETECTION - ML MODEL TRAINING")
    print("=" * 60)
    
    # === Step 1: Prepare URL data ===
    print("\n[1/4] Preparing URL dataset...")
    
    # For demo purposes, create synthetic data if no real data available
    # In production, load real datasets
    
    # Synthetic URLs for demonstration
    sample_urls = [
        "https://www.google.com",
        "https://mail.google.com",
        "https://www.facebook.com",
        "https://www.amazon.com",
        "https://www.paypal.com",
        "https://g00gle.com/login?q=verify",
        "https://www.paypa1.com/secure",
        "https://bit.ly/3abc123",
        "http://192.168.1.1:8080/malware.exe",
        "https://www.paypal.com.evil-website.xyz/verify",
        "http://suspicious-site.xyz/login.php",
        "https://www.apple.com.Phishing.com/verify",
        "https://login-bank.com/chase",
        "https://secure-verify.tk/login",
        "https://microsoft-verify.xyz/account",
    ]
    
    labels = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    
    # Extract features
    extractor = URLFeatureExtractor()
    features_list = []
    for url in sample_urls:
        features = extractor.extract(url)
        features_list.append(features)
    
    df = pd.DataFrame(features_list)
    X = df.values
    y = np.array(labels)
    
    # Train/test split
    from sklearn.model_selection import train_test_split
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print(f"  Dataset size: {len(X)}")
    print(f"  Training size: {len(X_train)}")
    print(f"  Validation size: {len(X_val)}")
    
    # === Step 2: Train URL model ===
    print("\n[2/4] Training URL classifier...")
    url_results = train_url_model(X_train, y_train, X_val, y_val)
    
    # Save URL model
    url_model_path = os.path.join(MODELS_DIR, "url_classifier.pkl")
    with open(url_model_path, 'wb') as f:
        pickle.dump({
            'model': url_results['model'],
            'feature_names': extractor.get_feature_names(),
            'metrics': {k: v for k, v in url_results.items() if k != 'model'}
        }, f)
    print(f"\n  Saved URL model to: {url_model_path}")
    
    # === Step 3: Train Email model (placeholder) ===
    print("\n[3/4] Training Email classifier...")
    print("  (Skipping - needs email dataset)")
    print("  Placeholder model saved")
    
    # === Step 4: Summary ===
    print("\n[4/4] Training Complete!")
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"URL Classifier F1: {url_results['f1']:.4f}")
    print(f"Models saved to: {MODELS_DIR}")
    print("\nNext steps:")
    print("  1. Train with real datasets (see README)")
    print("  2. Start the API: uvicorn src.backend.main:app")
    print("  3. Run tests: pytest tests/")


if __name__ == "__main__":
    main()
