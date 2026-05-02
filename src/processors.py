import pandas as pd
import os
import logging
import pyarrow
from src.decorators import monitor_execution

class CryptoProcessor:

    def __init__(self, data) -> None:
        self.df = pd.DataFrame(data)

    @monitor_execution
    def clean_data(self) -> pd.DataFrame:
        self.df = self.df[['id', 'symbol', 'current_price', 'market_cap', 'total_volume', 'last_updated']]
        self.df['last_updated'] = pd.to_datetime(self.df['last_updated']) # Convert last_updated column to datetime format
        return self.df
    
    @monitor_execution
    def filter_by_price(self, min_price:float) -> pd.DataFrame:
        self.df['current_price'] = pd.to_numeric(self.df['current_price'], errors='coerce') # Convert current_price to numeric, coercing errors to NaN
        return self.df[self.df['current_price'] >= min_price]
    
    @monitor_execution
    def save_to_csv(self, filename:str) -> None:

        directory = "data" 
        if not os.path.exists(directory):
            os.makedirs(directory) # Create the directory if it doesn't exist
            logging.info(f"Directory {directory} created.")

        filepath = os.path.join(directory, filename)
        self.df.to_csv(filepath, index=False)
        logging.info(f"Data saved to {filepath}")

    @monitor_execution
    def save_to_parquet(self, folder_name:str) -> None:
        directory = 'data'
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
                logging.info(f"Directory {directory} created.")
            full_path = os.path.join(directory, folder_name)
            self.df.to_parquet(full_path, index = False, engine = 'pyarrow', partition_cols = ['symbol'])  
            logging.info(f"Data saved to {full_path} in Parquet format.")  
        except Exception as e:
            logging.error(f"Error saving to Parquet: {str(e)}") # if there is an error during saving, I am logging the error message to see orchestration tools like Airflow or Prefect and understand what went wrong. This is crucial for debugging and maintaining the data pipeline.
    
