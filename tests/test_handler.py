
import pandas as pd
import pytest
import os
from src.etl_pipeline.handler import transform_sales_data, load_data_to_csv, read_external_csv_with_retry

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
    assert result.shape == (2, 8)
    assert "total_sales" in result.columns
    assert result["total_sales"].tolist() == [80.0, 80.0]

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

def test_load_data_to_csv(tmpdir):
    data = {
        "order_id": [1, 2],
        "customer_id": [101, 102],
        "product_id": [501, 502],
        "quantity": [2, 3],
        "price_per_item": [10.0, 20.0],
        "order_date": ["2023-09-01", "2023-09-02"],
    }
    df = pd.DataFrame(data)
    output_path = os.path.join(str(tmpdir), "test.csv")
    load_data_to_csv(df, output_path)
    assert os.path.exists(output_path)
    loaded_df = pd.read_csv(output_path)
    assert loaded_df.shape == (2, 6)

def test_read_external_csv_with_retry(tmpdir):
    # Create a dummy CSV file
    file_path = os.path.join(str(tmpdir), "test.csv")
    data = {"col1": [1, 2], "col2": [3, 4]}
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)

    # Test successful read
    read_df = read_external_csv_with_retry(file_path)
    assert not read_df.empty
    assert read_df.shape == (2, 2)

    # Test file not found
    non_existent_file = os.path.join(str(tmpdir), "non_existent.csv")
    read_df = read_external_csv_with_retry(non_existent_file, max_retries=1, delay=1)
    assert read_df is None

def test_transform_sales_data_error_handling():
    # Test with missing columns
    data = {"order_id": [1, 2]}
    df = pd.DataFrame(data)
    with pytest.raises(KeyError):
        transform_sales_data(df)

    # Test with incorrect data types
    data = {
        "order_id": [1, 2],
        "customer_id": [101, 102],
        "product_id": [501, 502],
        "quantity": [2, "a"],
        "price_per_item": [10.0, 20.0],
        "order_date": ["2023-09-01", "2023-09-02"],
    }
    df = pd.DataFrame(data)
    with pytest.raises(TypeError):
        transform_sales_data(df)
