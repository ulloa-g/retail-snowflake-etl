import pandas as pd

def extract_data(file_path):
    """
    Extract data from a CSV file and return a pandas DataFrame.
    
    Parameters:
    file_path (str): The path to the CSV file.
    
    Returns:
    pd.DataFrame: DataFrame containing the extracted data.
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error extracting data from {file_path}: {e}")
        return None

if __name__ == "__main__":
    file_path = './input_data/sales_data.csv'
    raw_df = extract_data(file_path)
