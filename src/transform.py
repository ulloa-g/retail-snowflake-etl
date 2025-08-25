import pandas as pd

def transform_data(df):
    """
    Transform the input DataFrame by cleaning and normalizing the data.
    
    Parameters:
    df (pd.DataFrame): The raw input DataFrame.
    
    Returns:
    pd.DataFrame: The transformed DataFrame.
    """
    try:
        df = df.rename(columns=str.upper)
        df = df.rename(columns={
            'SALES_AMOUNT': 'AMOUNT_SOLD'
        })
        return df
    except Exception as e:
        print(f"Error transforming data: {e}")
        return None
