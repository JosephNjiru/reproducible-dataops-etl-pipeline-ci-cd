import pandas as pd
import pytest
from src.etl_pipeline.handler import transform_sales_data

def test_successful_transformation():
    data = {
        "order_id": [1, 2],
        "customer_id": [101, 102],
        "product_id": [501, 502],
        "quantity": [2, 3],
        "price_per_item": [10.0, 20.0],
        "order_date": ["2023-09-01", "2023-09-02"],
    }
    df = pd.DataFrame(data)
    result = transform_sales_data(df)
    assert "total_price" in result.columns
    assert result["total_price"].tolist() == [20.0, 60.0]
    assert pd.api.types.is_datetime64_any_dtype(result["order_date"])
    assert result.shape == (2, 7)

def test_zero_quantity_filter():
    data = {
        "order_id": [1, 2, 3],
        "customer_id": [101, 102, 103],
        "product_id": [501, 502, 503],
        "quantity": [2, 0, -1],
        "price_per_item": [10.0, 20.0, 30.0],
        "order_date": ["2023-09-01", "2023-09-02", "2023-09-03"],
    }
    df = pd.DataFrame(data)
    result = transform_sales_data(df)
    assert all(result["quantity"] > 0)
    assert result.shape[0] == 1
    assert result.iloc[0]["order_id"] == 1

def test_empty_dataframe():
    columns = ["order_id", "customer_id", "product_id", "quantity", "price_per_item", "order_date"]
    df = pd.DataFrame(columns=columns)
    result = transform_sales_data(df)
    assert result.empty
    assert "total_price" in result.columns

