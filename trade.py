# Class for trading that contain buy and sell methods
from stock_news import Sentiment
from bank_account import BankAccount
from bank_account import BankAccount

class Trade:
    def __init__(self, stock_id):
        self.stock_id = stock_id
        self.balance = BankAccount().balance

    def buy(self, amount):
        # check if there's enough to buy that amount
        if self.amount <= 0.9 * self.balance:
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