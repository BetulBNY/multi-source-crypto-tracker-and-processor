import logging
from ingestors import CryptoAPIIngestor
from processors import CryptoProcessor


def main():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1"
    ingestor = CryptoAPIIngestor(url)
    data =  ingestor.fetch_data()

    if not data:
        logging.error("No data fetched from the API. Exiting the program.")
        stop_execution = True

    processor = CryptoProcessor(data)

    cleaned_data = processor.clean_data()
    filter_price = processor.filter_by_price(1000) 
    save_to_csv = processor.save_to_csv("crypto_data.csv")
    save_to_parquet = processor.save_to_parquet("crypto_partitioned.parquet")