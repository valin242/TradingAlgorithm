# Using LLM to develop sentiment analysis about a particlular stock
# Date implemented
# import language model from hugging face focused on market sentiment
# for training, can we find articles by specific dates

class Sentiment:
    def __init__(self, stock_id, date="today", past_date=None):
        self.stock_id = stock_id
        self.date = date # defualt today when looking at real time data
        self.past_date = past_date # datetime format as input
        

    def sentiment_ml(self):
        '''
        Function that uses a LLM to determine the sentiment based on articles about a particle stock
        LLM Used:
        Based on information from the News class below
        '''
        pass

class News(Sentiment): # Make this class a child class of Sentiment class
    def __init__(self):
        pass

    def get_news(self):
        if self.past_date == None: # excute with the current date
            pass
        else: # excute with the past_date value
            pass


    def store_news(self):
        pass


def main():
    '''
    Function to test the output of our model using predetermine values
    '''
    pass

if "__name__" == "__main__":
    main()