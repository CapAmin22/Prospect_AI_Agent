import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    APOLLO_API_KEY = os.getenv("APOLLO_API_KEY")
    HUNTER_API_KEY = os.getenv("HUNTER_API_KEY")
    
    DB_PATH = os.getenv("DB_PATH", "data/prospects.db")
    OUTPUT_DIR = os.getenv("OUTPUT_DIR", "data/output")
    CONFIDENCE_THRESHOLD = int(os.getenv("CONFIDENCE_THRESHOLD", 65))
    
    # Rate limiting
    API_DELAY = 3  # seconds between requests

settings = Settings()
