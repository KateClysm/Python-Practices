import sqlite3
from pathlib import Path

DB_PATH = Path("database/data_db.db")

def get_connection():
    return sqlite3.connect(DB_PATH)