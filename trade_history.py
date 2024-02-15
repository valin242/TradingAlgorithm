# This module makes a buy/sell recommendation based on history of stock prices
# Fine tune a finance LLM (as oppose to building from scratch)

# import LLM from hugging face
import ccxt # read up on this (used for crypto which may be it's own separate file)
import pandas as pd
import alpaca_trade_api as tradeapi # readup on this as well
import logging
import sys

# Create custom logger
logger = logging.getLogger(__name__)

# Create handlers
# file_handler = logging.FileHandler('trade_history_file.log')
stream_handler = logging.StreamHandler(sys.stdout)
# file_handler.setLevel(logging.INFO)
stream_handler.setLevel(logging.INFO)

# Create formatters and add to handlers
stream_format = logging.Formatter('%(levelname)s: %(message)s')
# file_format = logging.Formatter('[%(asctime)s] %(name)s: %(levelname)s: %(message)s')
stream_handler.setFormatter(stream_format)
# file_handler.setFormatter(file_format)

# Add handlers to the logger
logger.addHandler(stream_handler)
# logger.addHandler(file_handler)

class TradeHistory:
    def __init__(self, symbol, timeframe, limit):
        self.symbol = symbol
        self.timeframe = timeframe # 1m, 1h, 4h, 1d, etc.
        self.limit = limit # number of historical datapoints to fetch
    
    # To import historical data on a specific crypto (CCXT)
    def import_crypto_data(self):
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

if "__name__" == "__main__":
    main()