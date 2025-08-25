import pandas as pd
import os

import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas

from extract import extract_data
from transform import transform_data

def load_data(df):
    """
    Load the transformed DataFrame into a Snowflake table.
    
    Parameters:
    df (pd.DataFrame): The transformed DataFrame to be loaded.
    
    Returns:
    bool: True if load was successful, False otherwise.
    """
    try:
        # Establish Snowflake connection
        conn = snowflake.connector.connect(
            user=os.getenv('SF_USER'),
            password=os.getenv('SF_PASSWORD'),
            account=os.getenv('SF_ACCOUNT'),
            warehouse=os.getenv('SF_WAREHOUSE'),
            database='RETAIL_DW',
            schema='RAW'
        )
        
        # Load data into Snowflake
        success, nchunks, nrows, _ = write_pandas(
            conn=conn,
            df=df,
            table_name='FACT_SALES',
            database='RETAIL_DW',
            schema='RAW'
        )
        conn.close()
        
        if success:
            print(f"Successfully loaded {nrows} rows into Snowflake.")
            return True
        else:
            print("Failed to load data into Snowflake.")
            return False
    except Exception as e:
        print(f"Error loading data into Snowflake: {e}")
        return False

if __name__ == "__main__":
    #file_path = './input_data/sales_data.csv'
    #raw_df = extract_data(file_path)
    #cleaned_df = transform_data(raw_df)
    data = {
    "SALE_ID": [1, 2, 3],
    "DATE_ID": ["2025-08-01", "2025-08-02", "2025-08-03"],
    "PRODUCT_ID": [101, 102, 103],
    "REGION_ID": [1, 2, 3],
    "SALES_REP_ID": [11, 12, 13],
    "QUANTITY_SOLD": [5, 3, 8],
    "AMOUNT_SOLD": [500.0, 300.0, 800.0],
    "DISCOUNT": [50.0, 0.0, 80.0],
    "PAYMENT_METHOD": ["CREDIT_CARD", "CASH", "TRANSFER"],
    "SALES_CHANNEL": ["ONLINE", "STORE", "ONLINE"]
    }
    df_test = pd.DataFrame(data)
    load_data(df_test)