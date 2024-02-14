# This module makes a buy/sell recommendation based on history of stock prices
# Fine tune a finance LLM (as oppose to building from scratch)

# import LLM from hugging face
import ccxt # read up on this
import pandas as pd
import alpaca_trade_api as tradeapi # readup on this as well

class TradeHistory:
    def __init__(self, symbol, timeframe, limit):
        self.symbol = symbol
        self.timeframe = timeframe # 1m, 1h, 4h, 1d, etc.
        self.limit = limit # number of historical datapoints to fetch
        pass

    def import_data(self):
        exchange = ccxt.binance() # pick the exchange to use
        ohlcv = exchange.fetch_ohlcv(self.symbol, self.timeframe, self.limit) # open, high, low, close price, volume
        df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        return df.set_index('timestamp')


# Running from bash command line
def main():
    pass

if "__name__" == "__main__":
    main()