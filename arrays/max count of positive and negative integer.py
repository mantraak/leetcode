# Intuition

The problem asks us to determine whether there are more positive numbers or negative numbers in the array and return the larger count. Since zero is neither positive nor negative, it should not be counted.

# Approach

1. Initialize two counters:

   * `cnt` for positive numbers.
   * `count` for negative numbers.
2. Traverse through each element in the array.
3. If the number is greater than zero, increment `cnt`.
4. If the number is less than zero, increment `count`.
5. Compare both counters and return the larger one.

# Complexity

* Time complexity:

  * **O(n)** because we traverse the array once.

* Space complexity:

  * **O(1)** since only two variables are used regardless of input size.

# Code

```python
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        cnt = count = 0

        for i in nums:
            if i > 0:
                cnt += 1
            elif i < 0:
                count += 1

        if cnt > count:
            return cnt
        else:
            return count
```
