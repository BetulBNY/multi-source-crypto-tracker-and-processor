import logging
import sys
import os
from ingestors import CryptoAPIIngestor
from processors import CryptoProcessor
from dotenv import load_dotenv

def main():
    print("--- Pipeline Başladı ---")

    load_dotenv() # Load environment variables from .env file
    url = os.getenv("CRYPTO_API_URL") 
    min_price_filter = float(os.getenv("MIN_PRICE_FILTER", 1000)) 

    ingestor = CryptoAPIIngestor(url)

    print("Veri çekiliyor...")
    data =  ingestor.fetch_data()

    if not data:
        logging.error("No data fetched from the API. Exiting the program.")
        sys.exit(1) # Exit the program with a non-zero status to indicate an error

    processor = CryptoProcessor(data)

    processor.clean_data()
    filtered_df = processor.filter_by_price(min_price_filter) # Im storing the filtered data in a variable for later use.
    processor.save_to_csv("crypto_data.csv")
    processor.save_to_parquet("crypto_partitioned.parquet")
    print("--- Pipeline Başarıyla Tamamlandı ---")

if __name__ == "__main__":
    main()