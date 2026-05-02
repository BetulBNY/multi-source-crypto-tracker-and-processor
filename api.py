import pandas as pd
import os
from fastapi import FastAPI, HTTPException

app = FastAPI()
DATAPATH = "data/crypto_data.csv"

@app.get("/")
def home():
    return {"message": "Welcome to Crypto Tracker API", "status": "active"}

@app.get("/cryptos")
def get_cryptos():
    """All processed data is returned as JSON."""
    if os.path.exists(DATAPATH):
        df = pd.read_csv(DATAPATH)
        return df.to_dict(orient="records") # Convert the Pandas DataFrame to a list of dictionaries for JSON response
    else:
        raise HTTPException(status_code=404, detail="Data file not found")  
    

@app.get("cryptos/expensive")
def get_expensive_cryptos():
    if not os.path.exists(DATAPATH):
        raise HTTPException(status_code=404, detail="Data file not found"),
        
    df = pd.read_csv(DATAPATH)
    expensice_cryptos = df[df['current_price'] >= 1000]
    return expensice_cryptos.to_dict(orient="records")