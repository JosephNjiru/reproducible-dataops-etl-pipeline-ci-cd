def hello():
    return "Hello from etl_pipeline!"

import pandas as pd
from pandas import DataFrame
from typing import Any
import time

def hello():
    return "Hello from etl_pipeline!"

def read_external_csv_with_retry(filepath, max_retries=3, delay=2):
    """
    Reads a CSV file with retry logic for transient errors.
    Args:
        filepath (str): Path to CSV file.
        max_retries (int): Number of retry attempts.
        delay (int): Delay in seconds between retries.
    Returns:
        pd.DataFrame: Loaded DataFrame or None if failed.
    """
    for attempt in range(1, max_retries + 1):
        try:
            df = pd.read_csv(filepath)
            print(f"Successfully read {filepath} on attempt {attempt}")
            return df
        except Exception as e:
            print(f"Error reading {filepath} (attempt {attempt}): {e}")
            if attempt < max_retries:
                time.sleep(delay)
            else:
                print(f"Failed to read {filepath} after {max_retries} attempts.")
                return None

def transform_sales_data(df: DataFrame) -> DataFrame:
    """
    Transforms sales data for Zenith Active e-commerce ETL pipeline.

    1. Calculates total_price as quantity * price_per_item.
    2. Converts order_date from string to datetime.
    3. Filters out rows where quantity <= 0.

    Args:
        df (pd.DataFrame): Input DataFrame with columns order_id, customer_id, product_id, quantity, price_per_item, order_date.

    Returns:
        pd.DataFrame: Transformed DataFrame with total_price column, order_date as datetime, and filtered rows.
    """
    df = df.copy()
    df["total_price"] = df["quantity"] * df["price_per_item"]
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    df = df[df["quantity"] > 0]
    # Ensure 'total_sales' column exists as a scalar for all rows
    total_sales_value = df["total_price"].sum()
    df["total_sales"] = total_sales_value
    return df

if __name__ == '__main__':
    print(hello())
    # Example usage of error handling and retry
    # Example usage only; does not run during import for tests
    try:
        df = read_external_csv_with_retry('external_sales_data.csv')
        if df is not None:
            df_transformed = transform_sales_data(df)
            print(df_transformed.head())
    except Exception as e:
        print(f"Main block error: {e}")
