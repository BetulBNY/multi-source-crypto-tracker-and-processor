from typing import List, Dict, Any

import requests
import logging
from abc import ABC, abstractmethod # For creating abstract base classes 
from decorators import monitor_execution
# Template class
class AbstractBaseIngestor(ABC): # This is an abstract base class for data ingestors. It defines the structure and common functionality that all ingestors should have.
    
    @abstractmethod # means we cannot use this method directly, we must implement it in a subclass.
    def fetch_data(self) -> List[Dict[str, Any]]: # A list of dictionaries with any values inside
        """
        Abstract method to fetch data. Must be implemented by subclasses.
        """
        pass

class CryptoAPIIngestor(AbstractBaseIngestor):

    def __init__(self, url:str):
        if not url.startswith("http"):
            raise ValueError("Invalid URL provided. URL must start with http or https.")
        self.url = url

    @monitor_execution
    def fetch_data(self) -> List[Dict[str, Any]]:
        try:
            response = requests.get(self.url, timeout=10) # timeout to prevent hanging
            response.raise_for_status() # Raise an HTTPError for bad responses (4xx and 5xx)
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"API error for URL {self.url}: {str(e)}") # Log the error with URL information
            return []



