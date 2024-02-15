# This module makes a buy/sell recommendation based on history of stock prices
# Fine tune a finance LLM (as oppose to building from scratch)

# import LLM from hugging face
import ccxt # read up on this (used for crypto which may be it's own separate file)
import pandas as pd
import alpaca_trade_api as tradeapi # readup on this as well
from alpaca.data.historical import CryptoHistoricalDataClient
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame
from datetime import datetime
import logging
import sys

# Create custom logger
logger = logging.getLogger(__name__)

# Create handlers
# file_handler = logging.FileHandler('trade_history_file.log')
stream_handler = logging.StreamHandler(sys.stdout)
# file_handler.setLevel(logging.INFO)
stream_handler.setLevel(level=logging.INFO)

# Create formatters and add to handlers
stream_format = logging.Formatter('%(levelname)s: %(message)s')
# file_format = logging.Formatter('[%(asctime)s] %(name)s: %(levelname)s: %(message)s')
stream_handler.setFormatter(stream_format)
# file_handler.setFormatter(file_format)

# Add handlers to the logger
logger.addHandler(stream_handler)
# logger.addHandler(file_handler)

# No keys required for crypto data
client = CryptoHistoricalDataClient()

class TradeHistory:
    def __init__(self, symbol, timeframe, start=None, end=None, limit=None):
        self.symbol = symbol
        self.timeframe = timeframe # min, h, day, etc.
        self.start = start
        self.end = end
        self.limit = limit # number of historical datapoints to fetch
    
    # Import historical crypto data with Alpaca and return as a dataframe
    def import_crypto_data(self):
        try:
            request_params = CryptoBarsRequest(
                symbol_or_symbols=[self.symbol],
                timeframe=self.timeframe,
                start=self.start,
                limit=self.limit,
                #T00:00:00Z,
                end=self.end,
                #T00:00:00Z"
            )
            logger.info("Crypto Request sent successfully.")
        except:
            logger.warning("Missing a parameter or Incorrect symbol")
    

        # Retrieve daily bars for crypto in a dataframe
        crypto_bars = client.get_crypto_bars(request_params)
        # convert to dataframe
        return crypto_bars.df


    # To import historical data on a specific crypto (using CCXT)
    def import_crypto_data_ccxt(self):
        exchange = ccxt.binance() # pick the exchange to use
        ohlcv = exchange.fetch_ohlcv(self.symbol, self.timeframe, self.limit) # open, high, low, close price, volume
        df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        return df.set_index('timestamp')
    
    # To import hisotrical data on a specific stock (Alpaca)
    def import_stock_data(self):
        # Convert to dataframe for easy processing
        pass


# Running from bash command line
def main():
    tsla_hist = TradeHistory('tsla', 1, 100)
    tsla_hist_df = tsla_hist.import_stock_data()
    btc_hist = TradeHistory("BTC/USD", TimeFrame.Day, datetime(2023, 9, 1), datetime(2023, 9, 7))
    btc_hist_df = btc_hist.import_crypto_data()
    print(btc_hist_df.head())

if __name__ == "__main__":
    main()