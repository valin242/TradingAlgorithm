# File where the LLMs are actually trained
# This class can also be called for reinforcment learning after the initial training is complete
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

class AlgoTrain:
    def __init__(self, stock_id):
        pass

    def init_model():
        pass

    def update(self):
        pass

    def reinforcement(self):
        '''
        Based on realtime or more historic data, the alogrithm is reinforced based on how well our preditions did
        Updates from the update function are stored until ready to use for reinforcement learning/further fine tuning
        Set frequency of training:
        '''
        pass

    def new_model():
        pass