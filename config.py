import os

# =============================================================================
# 🎯 PRESENTATION NOTE - CODE QUALITY & CONFIGURATION REQUIREMENT 
# This file demonstrates:
# - MYSQL DATABASE CONFIGURATION 
# =============================================================================

class Config:
    """Base configuration class"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-here'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_SORT_KEYS = False

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    # MYSQL DATABASE CONFIGURATION REQUIREMENT
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql+mysqlconnector://root:13Agustus@localhost/ecommerce_api'  # REQ4: MySQL connection

# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}