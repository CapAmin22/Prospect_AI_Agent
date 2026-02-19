import sqlite3
import os
from config.settings import settings

def get_connection():
    os.makedirs(os.path.dirname(settings.DB_PATH), exist_ok=True)
    conn = sqlite3.connect(settings.DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    
    # Brand Profiles
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS brand_profiles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company_name TEXT UNIQUE,
            who_we_are TEXT,
            what_we_do TEXT,
            why_us TEXT,
            how_we_do_it TEXT,
            manually_edited INTEGER DEFAULT 0
        )
    ''')
    
    # Competitors
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS competitors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            brand_id INTEGER,
            name TEXT,
            tier TEXT,
            description TEXT,
            FOREIGN KEY (brand_id) REFERENCES brand_profiles (id)
        )
    ''')
    
    # Prospects
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS prospects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            email TEXT UNIQUE,
            linkedin_url TEXT,
            job_title TEXT,
            company_name TEXT,
            confidence_score REAL,
            source TEXT
        )
    ''')
    
    # Pitch Sequences
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pitch_sequences (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            prospect_id INTEGER,
            touch_1 TEXT,
            touch_2 TEXT,
            touch_3 TEXT,
            FOREIGN KEY (prospect_id) REFERENCES prospects (id)
        )
    ''')
    
    conn.commit()
    conn.close()
