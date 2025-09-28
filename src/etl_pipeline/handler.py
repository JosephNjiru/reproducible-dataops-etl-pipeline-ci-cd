def hello():
    return "Hello from etl_pipeline!"

import pandas as pd
from pandas import DataFrame
from typing import Any

def hello():
    return "Hello from etl_pipeline!"

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
    return df

if __name__ == '__main__':
    print(hello())
