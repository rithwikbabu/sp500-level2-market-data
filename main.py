import time
from polygon import RESTClient
import pickle
# uAZtAwym4JxD3U9wTJfvlW3fx12XScLM


def getData(client, ticker, start_date, end_date):
    aggs = []
    for a in client.list_aggs(ticker=ticker, multiplier=5, timespan="minute", from_=start_date, to=end_date, limit=50000):
        aggs.append(a)

    return aggs


def save_data(ticker, data):
    filename = f"data/{ticker}.pkl"

    with open(filename, "wb") as fp:
        pickle.dump(data, fp)

    print(f"Saved data for {ticker} to {filename}.")


def get_next_ticker():
    try:
        with open("tickers_remaining.csv", "r") as fp:
            tickers = [line.strip() for line in fp if line.strip()]
    except FileNotFoundError:
        print("The file 'tickers_remaining.csv' does not exist.")
        return

    if not tickers:
        print("All tickers have been processed.")
        return

    ticker = tickers.pop(0)

    with open("tickers_remaining.csv", "w") as fp:
        fp.write("\n".join(tickers))

    print(f"Removed {ticker} the tickers file.")

    return ticker


def run(api_key):
    client = RESTClient(api_key=api_key)

    ticker = get_next_ticker()

    try:
        data = getData(client, ticker, "2021-12-01", "2023-11-01")

        save_data(ticker, data)

    except Exception as e:
        print(f"Error processing {ticker}: {str(e).split()[0]}")
        print("Adding ticker back to the list.")

        with open("tickers_remaining.csv", "a") as fp:
            fp.write(f"\n{ticker}")

if __name__ == "__main__":
    run("uAZtAwym4JxD3U9wTJfvlW3fx12XScLM")
    run("gjwnimbmBf2p465awj1DI3ln4JkeJ6Re")