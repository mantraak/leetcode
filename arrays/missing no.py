# Intuition

The array contains `n` distinct numbers taken from the range `[0, n]`. Since exactly one number is missing, we can calculate the expected sum of all numbers from `0` to `n` and subtract the actual sum of the array. The difference will be the missing number.

# Approach

1. Find the length of the array `n`.

2. Calculate the actual sum of elements in the array.

3. Use the formula for the sum of the first `n` natural numbers:

   `n * (n + 1) / 2`

4. Subtract the actual sum from the expected sum.

5. Return the result as the missing number.

# Complexity

* Time complexity:

  * **O(n)** because we traverse the array once to compute the sum.

* Space complexity:

  * **O(1)** since only a few variables are used.

# Code

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l, s = len(nums), sum(nums)
        e = l * (l + 1) // 2
        return e - s
```
