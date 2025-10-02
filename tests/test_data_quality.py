import pandas as pd
import great_expectations as gx
from src.etl_pipeline.handler import transform_sales_data

def test_data_quality_with_suite():
    # 1. Prepare the data
    data = {
        'order_id': [1, 2, 3],
        'customer_id': [101, 102, 103],
        'product_id': [501, 502, 503],
        'quantity': [10, 5, 3],
        'price_per_item': [2.5, 5.0, 2.5],
        'order_date': ['2025-09-01', '2025-09-02', '2025-09-03']
    }
    df = pd.DataFrame(data)
    transformed_df = transform_sales_data(df)

    # 2. Instantiate a Validator directly from the in-memory DataFrame
    # This bypasses the entire DataContext and file system.
    validator = gx.from_pandas(transformed_df)

    # 3. Define expectations programmatically on the validator
    validator.expect_column_values_to_not_be_null(column="order_id")
    validator.expect_column_values_to_be_greater_than_or_equal_to(column="total_price", min_value=0)
    validator.expect_column_values_to_not_be_null(column="order_date")
    validator.expect_column_values_to_not_be_null(column="product_id")

    # 4. Run the validation
    result = validator.validate()

    # 5. Assert that the validation was successful
    assert result["success"] is True