import pandas as pd
import great_expectations as ge
from src.etl_pipeline.handler import transform_sales_data

def test_data_quality():
    # Sample data
    data = {
        'order_id': [1, 2, 3],
        'product': ['Widget', 'Gadget', 'Widget'],
        'quantity': [10, 5, 3],
        'price': [2.5, 5.0, 2.5],
        'order_date': ['2025-09-01', '2025-09-02', '2025-09-03']
    }
    df = pd.DataFrame(data)
    transformed = transform_sales_data(df)
    ge_df = ge.from_pandas(transformed)
    # Expect total_sales to be non-negative
    assert ge_df.expect_column_values_to_be_between('total_sales', min_value=0)['success']
    # Expect no missing values in product
    assert ge_df.expect_column_values_to_not_be_null('product')['success']
