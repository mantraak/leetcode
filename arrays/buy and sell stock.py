# Intuition

To maximize profit, we need to buy at the lowest price and sell at a higher price that comes after it. Instead of checking every possible pair, we can keep track of the minimum price seen so far and calculate the profit if we sell on the current day.

# Approach

1. Initialize `min_price` with the first stock price.
2. Initialize `max_profit` as 0.
3. Traverse the remaining prices.
4. If the current price is lower than `min_price`, update `min_price`.
5. Otherwise, calculate the profit by selling at the current price.
6. Update `max_profit` if the current profit is greater.
7. Return `max_profit` after processing all prices.

# Complexity

* Time complexity:

  * **O(n)** because we traverse the array only once.

* Space complexity:

  * **O(1)** since only a few variables are used.

# Code

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit
```
