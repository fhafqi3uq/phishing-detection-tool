"""
URL Feature Extraction Module
Extracts features from URLs for ML classification
"""

import re
import math
from urllib.parse import urlparse
from typing import Dict, List
import pandas as pd


class URLFeatureExtractor:
    """Extract features from URLs for phishing detection"""
    
    SUSPICIOUS_KEYWORDS = [
        'login', 'signin', 'sign-in', 'verify', 'verification',
        'account', 'update', 'secure', 'securely', 'banking',
        'confirm', 'password', 'credential', 'authenticate',
        'auth', 'validation', 'validate', 'security', 'alert',
        'suspended', 'unusual', 'prize', 'winner', 'lottery',
        'bitcoin', 'crypto', 'wallet', 'paypal', 'apple', 'microsoft',
        'google', 'facebook', 'amazon', 'netflix', 'ebay'
    ]
    
    SUSPICIOUS_TLDS = ['xyz', 'top', 'club', 'online', 'site', 'website', 'work', 'ru', 'cn']
    
    SHORTENER_DOMAINS = [
        'bit.ly', 'tinyurl.com', 'goo.gl', 't.co', 'ow.ly',
        'is.gd', 'buff.ly', 'adf.ly', 'j.mp', 'tr.im',
        'tiny.cc', 'lnkd.in', 'db.tt', 'qr.ae', 'cur.lv'
    ]
    
    def __init__(self):
        self.feature_names = None
    
    def extract(self, url: str) -> Dict:
        """Extract all features from a URL"""
        features = {}
        
        # Parse URL
        try:
            parsed = urlparse(url)
        except Exception:
            return self._empty_features()
        
        domain = parsed.netloc
        path = parsed.path
        query = parsed.query
        
        # === Basic Length Features ===
        features['url_length'] = len(url)
        features['domain_length'] = len(domain)
        features['path_length'] = len(path) if path else 0
        features['query_length'] = len(query) if query else 0
        
        # === Character Count Features ===
        features['num_dots'] = url.count('.')
        features['num_hyphens'] = url.count('-')
        features['num_underscores'] = url.count('_')
        features['num_slashes'] = url.count('/')
        features['num_question_marks'] = url.count('?')
        features['num_equals'] = url.count('=')
        features['num_at'] = url.count('@')
        features['num_and'] = url.count('&')
        features['num_exclamation'] = url.count('!')
        features['num_tilde'] = url.count('~')
        features['num_percent'] = url.count('%')
        features['num_double_slash'] = url.count('//')
        features['num_special_chars'] = len(re.findall(r'[^a-zA-Z0-9]', url))
        
        # === Protocol Features ===
        features['has_https'] = 1 if parsed.scheme == "https" else 0
        features['has_http'] = 1 if parsed.scheme == "http" else 0
        
        # === IP Address Features ===
        features['has_ip'] = 1 if re.match(r'\d+\.\d+\.\d+\.\d+', domain) else 0
        
        # === Domain Features ===
        features['subdomain_count'] = self._count_subdomains(domain)
        features['num_subdomains'] = domain.count('.') - 1 if domain.count('.') > 1 else 0
        features['domain_has_numbers'] = 1 if re.search(r'\d', domain) else 0
        features['tld'] = self._get_tld(domain)
        features['tld_suspicious'] = 1 if features['tld'] in self.SUSPICIOUS_TLDS else 0
        
        # === Path Features ===
        features['path_depth'] = path.count('/') if path else 0
        features['path_has_numbers'] = 1 if re.search(r'\d', path) else 0
        features['encoded_chars'] = url.count('%')
        
        # === Entropy (Shannon) ===
        features['url_entropy'] = self._calculate_entropy(url)
        features['domain_entropy'] = self._calculate_entropy(domain)
        
        # === Suspicious Keywords ===
        features['suspicious_keywords_count'] = self._count_suspicious_keywords(url)
        features['has_suspicious_keyword'] = 1 if features['suspicious_keywords_count'] > 0 else 0
        
        # === URL Shortener Detection ===
        features['is_shortened'] = 1 if self._is_shortened_url(domain) else 0
        
        # === Brand Impersonation ===
        features['brand_impersonation'] = self._detect_brand_impersonation(url)
        
        # === Security Indicators ===
        features['has_port'] = 1 if re.search(r':\d+', domain) else 0
        features['has_fragment'] = 1 if '#' in url else 0
        features['has_data_uri'] = 1 if 'data:' in url else 0
        features['has javascript'] = 1 if 'javascript:' in url.lower() else 0
        
        # === Statistical Features ===
        features['digit_to_letter_ratio'] = self._digit_letter_ratio(url)
        features['vowel_ratio'] = self._vowel_ratio(domain)
        
        self.feature_names = list(features.keys())
        return features
    
    def _empty_features(self) -> Dict:
        """Return empty features dict"""
        return {name: 0 for name in self.get_feature_names()}
    
    def get_feature_names(self) -> List[str]:
        """Get list of all feature names"""
        if self.feature_names is None:
            self.extract("http://example.com")  # Dummy call to init
        return self.feature_names
    
    def _count_subdomains(self, domain: str) -> int:
        """Count number of subdomains"""
        parts = domain.split('.')
        if len(parts) > 2:
            return len(parts) - 2
        return 0
    
    def _get_tld(self, domain: str) -> str:
        """Extract TLD from domain"""
        parts = domain.split('.')
        if len(parts) >= 2:
            return parts[-1].lower()
        return ''
    
    def _calculate_entropy(self, text: str) -> float:
        """Calculate Shannon entropy of text"""
        if not text:
            return 0
        
        from collections import Counter
        prob = [float(count) / len(text) for count in Counter(text).values()]
        entropy = -sum(p * math.log2(p) for p in prob if p > 0)
        return round(entropy, 4)
    
    def _count_suspicious_keywords(self, url: str) -> int:
        """Count suspicious keywords in URL"""
        url_lower = url.lower()
        count = 0
        for kw in self.SUSPICIOUS_KEYWORDS:
            count += url_lower.count(kw)
        return count
    
    def _is_shortened_url(self, domain: str) -> bool:
        """Check if domain is a URL shortener"""
        return any(shortener in domain.lower() for shortener in self.SHORTENER_DOMAINS)
    
    def _detect_brand_impersonation(self, url: str) -> int:
        """Detect potential brand impersonation"""
        url_lower = url.lower()
        
        brands = {
            'google': ['g00gle', 'googIe', 'goog1e', 'googie', 'gogle', 'gooogle'],
            'facebook': ['faceb00k', 'facebook', 'facebok', 'facbook'],
            'paypal': ['paypa1', 'paypall', 'peypal'],
            'apple': ['app1e', 'apple', 'aple'],
            'microsoft': ['micros0ft', 'microsft', 'rnicrosoft'],
            'amazon': ['arnazon', 'amaz0n', 'amazn'],
        }
        
        for brand, typos in brands.items():
            if brand in url_lower:
                # Check if real domain or typo
                if not any(legit in url_lower for legit in [f'{brand}.com', f'{brand}.org']):
                    for typo in typos:
                        if typo in url_lower and brand not in url_lower.replace(typo, ''):
                            return 1
        return 0
    
    def _digit_letter_ratio(self, text: str) -> float:
        """Calculate ratio of digits to letters"""
        digits = sum(c.isdigit() for c in text)
        letters = sum(c.isalpha() for c in text)
        if letters == 0:
            return 0
        return round(digits / letters, 4)
    
    def _vowel_ratio(self, text: str) -> float:
        """Calculate ratio of vowels in text"""
        vowels = sum(1 for c in text.lower() if c in 'aeiou')
        if len(text) == 0:
            return 0
        return round(vowels / len(text), 4)


def extract_batch(urls: List[str]) -> pd.DataFrame:
    """Extract features from multiple URLs"""
    extractor = URLFeatureExtractor()
    features_list = []
    
    for url in urls:
        features = extractor.extract(url)
        features['url'] = url
        features_list.append(features)
    
    return pd.DataFrame(features_list)


if __name__ == "__main__":
    # Test
    extractor = URLFeatureExtractor()
    
    test_urls = [
        "https://www.google.com",
        "https://g00gle.com/login?q=verify",
        "https://bit.ly/3abc123",
        "http://192.168.1.1:8080/malware.exe",
        "https://www.paypal.com.evil-website.xyz/verify"
    ]
    
    for url in test_urls:
        features = extractor.extract(url)
        print(f"\n{url}")
        print(f"  Phishing score keywords: {features['suspicious_keywords_count']}")
        print(f"  URL entropy: {features['url_entropy']}")
        print(f"  Has IP: {features['has_ip']}")
        print(f"  Is shortened: {features['is_shortened']}")
        print(f"  Brand impersonation: {features['brand_impersonation']}")
