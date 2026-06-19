# backend/database.py

import os
import sqlite3
from datetime import datetime

# Database file ka path define kar rahe hain
DB_DIR = os.path.join(os.path.dirname(__file__), '..', 'database')
DB_PATH = os.path.join(DB_DIR, 'farming.db')

def init_db():
    """
    Database aur tables ko initialize karne ke liye function.
    Agar directory ya file nahi hogi, toh yeh create kar dega.
    """
    # Agar 'database' folder nahi hai toh banao
    if not os.path.exists(DB_DIR):
        os.makedirs(DB_DIR)
        
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Sensor logs store karne ke liye table creation
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sensor_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            temperature REAL NOT NULL,
            humidity REAL NOT NULL,
            moisture REAL NOT NULL,
            pump_status INTEGER NOT NULL,
            ai_reason TEXT NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()
    print("✓ Database setup completed successfully.")

def insert_log(temperature, humidity, moisture, pump_status, ai_reason):
    """
    IoT data aur AI ka decision database me save karne ke liye function.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    cursor.execute('''
        INSERT INTO sensor_logs (timestamp, temperature, humidity, moisture, pump_status, ai_reason)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (current_time, temperature, humidity, moisture, pump_status, ai_reason))
    
    conn.commit()
    conn.close()

def get_latest_logs(limit=10):
    """
    Frontend dashboard par dikhane ke liye latest records fetch karne ka function.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Latest entries upar dikhane ke liye ORDER BY id DESC lagaya hai
    cursor.execute('SELECT * FROM sensor_logs ORDER BY id DESC LIMIT ?', (limit,))
    rows = cursor.fetchall()
    
    conn.close()
    return rows

# Self-testing block (Sirf file ko direct run karke check karne ke liye)
if __name__ == "__main__":
    init_db()
    # Ek dummy test entry insert karke dekhte hain
    insert_log(32.5, 65.0, 22.1, 1, "Test entry: Soil is dry.")
    print("✓ Dummy log inserted. Latest record:", get_latest_logs(1))
