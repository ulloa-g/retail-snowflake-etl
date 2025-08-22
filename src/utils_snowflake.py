import os
from dotenv import load_dotenv
import snowflake.connector

# load environment variables from .env file
load_dotenv()

# Connect to Snowflake
def get_sf_connection():
    conn = snowflake.connector.connect(
        user=os.getenv('SF_USER'),
        password=os.getenv('SF_PASSWORD'),
        account=os.getenv('SF_ACCOUNT'),
        warehouse=os.getenv('SF_WAREHOUSE'),
        database=os.getenv('SF_DATABASE'),
        schema=os.getenv('SF_SCHEMA'),
        role=os.getenv('SF_ROLE')
    )
    return conn
