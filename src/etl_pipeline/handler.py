import pandas as pd
from pandas import DataFrame
from typing import Any
import time

def hello():
    '''
    Returns a simple greeting.
    '''
    return "Hello from etl_pipeline!"

def read_external_csv_with_retry(filepath: str, max_retries: int = 3, delay: int = 2) -> pd.DataFrame | None:
    '''
    Reads a CSV file with a retry mechanism to handle transient I/O errors.

    This function attempts to read a CSV file from the given filepath. If an error occurs,
    it will retry up to `max_retries` times, waiting for `delay` seconds between each attempt.

    Args:
        filepath (str): The path to the CSV file.
        max_retries (int): The maximum number of retry attempts.
        delay (int): The delay in seconds between retries.

    Returns:
        pd.DataFrame | None: The loaded DataFrame if successful, or None if all retries fail.
    '''
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
    '''
    Transforms the raw sales data from the e-commerce platform.

    This function performs the following transformations:
    1. Calculates the `total_price` for each order (quantity * price_per_item).
    2. Converts the `order_date` column to datetime objects.
    3. Filters out any orders with a quantity less than or equal to 0.
    4. Calculates the `total_sales` for the entire DataFrame and adds it as a new column.
       Note: The `total_sales` column will have the same value in every row.

    Args:
        df (pd.DataFrame): The input DataFrame with the raw sales data.

    Returns:
        pd.DataFrame: The transformed DataFrame.
    '''
    df = df.copy()
    df["total_price"] = df["quantity"] * df["price_per_item"]
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    df = df[df["quantity"] > 0]
    
    # Calculate the total sales for the entire DataFrame and add it as a new column.
    # This is done to provide a summary statistic for the entire dataset on each row.
    total_sales_value = df["total_price"].sum()
    df["total_sales"] = total_sales_value
    
    return df

def load_data_to_csv(df: DataFrame, output_path: str) -> None:
    '''
    Saves a DataFrame to a CSV file.

    Args:
        df (pd.DataFrame): The DataFrame to save.
        output_path (str): The path to the output CSV file.
    '''
    try:
        df.to_csv(output_path, index=False)
        print(f"Successfully saved data to {output_path}")
    except Exception as e:
        print(f"Error saving data to {output_path}: {e}")

if __name__ == '__main__':
    '''
    Main entry point for the ETL script.

    This block demonstrates the full ETL process:
    1. Reads the raw sales data from a CSV file.
    2. Transforms the data.
    3. Loads the transformed data into a new CSV file.
    '''
    print(hello())
    
    try:
        df = read_external_csv_with_retry('external_sales_data.csv')
        if df is not None:
            df_transformed = transform_sales_data(df)
            load_data_to_csv(df_transformed, 'transformed_sales_data.csv')
            print("\nTransformed Data Head:")
            print(df_transformed.head())
    except Exception as e:
        print(f"An error occurred in the main block: {e}")