import pandas as pd
from dotenv import load_dotenv
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
        load_dotenv('/home/gabriel/repos/retail-snowflake-etl/.env')
        conn = snowflake.connector.connect(
            user=os.getenv('SF_USER'),
            password=os.getenv('SF_PASSWORD'),
            account=os.getenv('SF_ACCOUNT'),
            warehouse=os.getenv('SF_WAREHOUSE'),
            database=os.getenv('SF_DATABASE'),
            schema='STG'
        )
        
        # Load data into Snowflake
        success, nchunks, nrows, _ = write_pandas(
            conn=conn,
            df=df,
            table_name='RAW_SALES',
            database=os.getenv('SF_DATABASE'),
            schema='STG'
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
    file_path = '../input_data/sales_data.csv'
    raw_df = extract_data(file_path)
    cleaned_df = transform_data(raw_df)
    load_data(cleaned_df)