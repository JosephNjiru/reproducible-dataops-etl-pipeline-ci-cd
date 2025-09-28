import sqlite3
import pandas as pd
import pytest
from src.etl_pipeline.handler import transform_sales_data

def setup_test_db():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE sales (
        order_id INTEGER PRIMARY KEY,
        product TEXT,
        quantity INTEGER,
        price_per_item REAL,
        order_date TEXT
    )''')
    cursor.executemany('INSERT INTO sales (product, quantity, price_per_item, order_date) VALUES (?, ?, ?, ?)', [
        ('Widget', 10, 2.5, '2025-09-01'),
        ('Gadget', 5, 5.0, '2025-09-02'),
        ('Widget', 3, 2.5, '2025-09-03'),
    ])
    conn.commit()
    return conn

def test_db_etl_integration():
    conn = setup_test_db()
    df = pd.read_sql_query('SELECT * FROM sales', conn)
    transformed = transform_sales_data(df)
    assert not transformed.empty
    assert 'total_sales' in transformed.columns
    conn.close()
