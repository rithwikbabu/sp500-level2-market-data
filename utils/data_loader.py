import requests
import pickle

BASE_PATH = "https://github.com/rithwikbabu/sp500-level2-market-data/raw/main/data/{ticker}.pkl"

with open("sp500_tickers.csv", "r") as fp:
    sp500 = set([line.strip() for line in fp if line.strip()])

for ticker in sp500:
    response = requests.get(BASE_PATH.format(ticker=ticker))
    if response.status_code == 200:
        # unpickle the data and print its length
        with open(f'{ticker}.pkl', 'wb') as f:
            data = pickle.load(response.content)
            print(f"{ticker}: {len(data)}")
            
