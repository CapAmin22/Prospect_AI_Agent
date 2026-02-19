import pandas as pd
from src.utils.database import get_connection
from config.settings import settings
import os

def export_verified_prospects(filename="verified_prospects.csv"):
    conn = get_connection()
    query = f"SELECT * FROM prospects WHERE confidence_score >= {settings.CONFIDENCE_THRESHOLD}"
    df = pd.read_sql_query(query, conn)
    
    os.makedirs(settings.OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(settings.OUTPUT_DIR, filename)
    
    df.to_csv(output_path, index=False)
    conn.close()
    return output_path
