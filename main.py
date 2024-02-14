# TradeAlgo
# @author: 2pitesh
# Main file to excute trading
# for the ML files, each stock is going to have it's own prediction model

# import necessary libraries
import pandas as pd
import numpy as np
from trade import Trade


stock_name = Trade()

def main():
    stock_tsla = Trade("TSLA")
    stock_btc = Trade("BTC")

if "__name__" == "__main__":
    main()