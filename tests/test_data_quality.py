import pandas as pd
import pandera as pa
from pandera.typing import Series
from src.etl_pipeline.handler import transform_sales_data

# 1. Define the data validation schema using Pandera
class TransformedSalesSchema(pa.SchemaModel):
    order_id: Series[int] = pa.Field(nullable=False)
    customer_id: Series[int] = pa.Field(nullable=False)
    product_id: Series[int] = pa.Field(nullable=False)
    quantity: Series[int] = pa.Field(gt=0)
    price_per_item: Series[float] = pa.Field(gt=0)
    order_date: Series[pd.Timestamp]
    total_price: Series[float] = pa.Field(ge=0, nullable=False)
    total_sales: Series[float] = pa.Field(ge=0, nullable=False)

    class Config:
        strict = True  # Ensures no unexpected columns are present
        coerce = True  # Coerces data types to the correct ones if possible

# 2. Define the pytest test function
def test_data_quality_with_pandera():
    # Prepare the data
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

    # Validate the transformed DataFrame against the schema
    # The test will automatically pass if no exception is raised
    TransformedSalesSchema.validate(transformed_df)