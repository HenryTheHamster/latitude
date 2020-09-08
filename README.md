## Problem

Suppose we could access yesterday's stock prices as a list, where:

* The indices are the time in minutes past trade opening time, which was 10:00am local time.
* The values are the price in dollars of the Latitude Financial stock at that time.
* So if the stock cost $5 at 11:00am, stock_prices_yesterday[60] = 5.

Write an *efficient function* that takes an array of stock prices and returns the best profit I could have made from 1 purchase and 1 sale of 1 Latitude Financial stock yesterday.

For example:
```js
var stock_prices_yesterday = [10, 7, 5, 8, 11, 9];

get_max_profit(stock_prices_yesterday)
# returns 6 (buying for $5 and selling for $11)
```

You must buy before you sell.
You may not buy and sell in the same time step (at least 1 minute must pass).

## Usage

```
from max_profit import max_profit

data = [10, 7, 5, 8, 11, 9]
max_profit(data)
// returns 6
```

To run the test suite:
```
python -m unittest discover -s tests
```

## Notes

It could be argued that `reduce` would offer even more efficiency in this case, however I believe that this solution offers better readabilty at marginal cost.