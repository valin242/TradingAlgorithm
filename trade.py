# Class for trading that contain buy and sell methods
from stock_news import Sentiment
from bank_account import BankAccount
from bank_account import BankAccount
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

class Trade:
    def __init__(self, stock_id):
        self.stock_id = stock_id
        self.balance = BankAccount().balance

    def buy(self, amount):
        # check if there's enough funds to buy that amount
        if amount >= 0.9 * self.balance:
            pass
        else:
            print("You do not have enough funds in your account")
            add_funds = input("Do you want to add more funds: Y/N")
            if add_funds == "Y":
                account = BankAccount()
                withdraw = input("How much do you want to withdraw from your account?")
                withdraw = int(withdraw)
                account.withdraw_funds(withdraw)
            else:
                pass

    def sell(self, amount):
        pass


def main():
    stock_id = "TSLA"
    stock = Trade(stock_id)
    decision = Sentiment(stock_id)
    if decision.sentiment_ml >= 0.65:
        stock.buy(50)

if __name__ == "__main__":
    main()