"""
Configuration loader for Camp Lakota WordPress Publisher
Loads and validates environment variables from .env file
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
env_path = Path(__file__).parent / '.env'
load_dotenv(dotenv_path=env_path)


class Config:
    """Configuration class for WordPress publisher"""
    
    # WordPress credentials
    WP_SITE_URL = os.getenv('WP_SITE_URL', '').rstrip('/')
    WP_USERNAME = os.getenv('WP_USERNAME', '')
    WP_APP_PASSWORD = os.getenv('WP_APP_PASSWORD', '')
    
    # Optional settings
    DRY_RUN = os.getenv('DRY_RUN', 'false').lower() == 'true'
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO').upper()
    
    # Paths
    BASE_DIR = Path(__file__).parent
    CONTENT_DIR = BASE_DIR / 'content'
    PAGES_DIR = CONTENT_DIR / 'pages'
    POSTS_DIR = CONTENT_DIR / 'posts'
    IMAGES_DIR = CONTENT_DIR / 'images'
    LOGS_DIR = BASE_DIR / 'logs'
    
    @classmethod
    def validate(cls):
        """Validate that required configuration is present"""
        errors = []
        
        if not cls.WP_SITE_URL:
            errors.append("WP_SITE_URL is not set in .env file")
        
        if not cls.WP_USERNAME:
            errors.append("WP_USERNAME is not set in .env file")
        
        if not cls.WP_APP_PASSWORD:
            errors.append("WP_APP_PASSWORD is not set in .env file")
        
        if errors:
            raise ValueError(
                "Configuration errors:\n" + "\n".join(f"  - {e}" for e in errors)
            )
        
        return True
    
    @classmethod
    def is_dry_run(cls):
        """Check if running in dry-run mode"""
        return cls.DRY_RUN
    
    @classmethod
    def get_api_url(cls, endpoint):
        """Get full WordPress API URL for endpoint"""
        return f"{cls.WP_SITE_URL}/wp-json/wp/v2/{endpoint}"
    
    @classmethod
    def ensure_directories(cls):
        """Ensure all required directories exist"""
        cls.PAGES_DIR.mkdir(parents=True, exist_ok=True)
        cls.POSTS_DIR.mkdir(parents=True, exist_ok=True)
        cls.IMAGES_DIR.mkdir(parents=True, exist_ok=True)
        cls.LOGS_DIR.mkdir(parents=True, exist_ok=True)


# Validate configuration on import
if __name__ != '__main__':
    try:
        Config.validate()
    except ValueError as e:
        print(f"\n⚠️  Configuration Error:\n{e}\n")
        print("Please create a .env file from env.example and fill in your credentials.")
