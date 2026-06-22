# Intuition
Each row in the `accounts` matrix represents a customer's wealth across different bank accounts. To find the richest customer, we calculate the total wealth of each customer and keep track of the maximum wealth encountered.

# Approach
1. Initialize a variable `a` to store the maximum wealth found so far.
2. Iterate through each customer's account list.
3. Calculate the customer's total wealth using `sum()`.
4. If the current wealth is greater than or equal to the maximum wealth, update `a`.
5. After checking all customers, return `a`.

# Complexity
- Time complexity:
  - **O(m × n)**, where `m` is the number of customers and `n` is the average number of accounts per customer.

- Space complexity:
  - **O(1)**, as only a few extra variables are used.

# Code
```python
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        a = 0

        for i in accounts:
            b = sum(i)
            if b >= a:
                a = b

        return a
