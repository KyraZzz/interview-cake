import math


def getMaxProfit(stock_prices):
    """
        Args:
            stock_prices: a list of stock prices indexed by time past trade opening time
        Returns:
            the best profit I could have made from one purchase and one sale of one share of Apple stock
    """
    if (len(stock_prices) < 2):
        return 0
    low = math.inf
    max_profit = -math.inf
    for i in stock_prices:
        max_profit = max(max_profit, i - low)
        low = min(low, i)

    return max_profit


if __name__ == '__main__':
    stock_prices = [10, 7, 5, 8, 11, 9]
    print(getMaxProfit(stock_prices))
    stock_prices = [10, 7, 5, 4, 3, 2]
    print(getMaxProfit(stock_prices))
    stock_prices = [3]
    print(getMaxProfit(stock_prices))
