
def max_profit(prices):
    max_profit = prices[1] - prices[0]
    min_price = prices[0]

    for i in range(1, len(prices)):
        if (prices[i] - min_price > max_profit):
            max_profit = prices[i] - min_price

        if (prices[i] < min_price):
            min_price = prices[i]

    return max(max_profit, 0)
