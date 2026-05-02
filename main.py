import logging
import sys
from ingestors import CryptoAPIIngestor
from processors import CryptoProcessor


def main():
    print("--- Pipeline Başladı ---")

    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1"
    ingestor = CryptoAPIIngestor(url)

    print("Veri çekiliyor...")
    data =  ingestor.fetch_data()

    if not data:
        logging.error("No data fetched from the API. Exiting the program.")
        sys.exit(1) # Exit the program with a non-zero status to indicate an error

    processor = CryptoProcessor(data)

    processor.clean_data()
    filtered_df = processor.filter_by_price(1000) # Im storing the filtered data in a variable for later use.
    processor.save_to_csv("crypto_data.csv")
    processor.save_to_parquet("crypto_partitioned.parquet")
    print("--- Pipeline Başarıyla Tamamlandı ---")

if __name__ == "__main__":
    main()