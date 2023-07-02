import alpaca_trade_api as tradeapi
import time


def get_current_positions():
    api = tradeapi.REST()  # insert credentials
    current_portfolio = api.list_positions()

    # Print the quantity of shares for each position.
    for position in current_portfolio:
        print("{} shares of {}".format(position.qty, position.symbol))


def supervise_bought_stocks():
    while True:
        # open_positions = get_current_positions()
        time.sleep(100)
