# Intuition

The goal is to find the longest sequence of consecutive `1`s in the array. We can keep track of the current streak of `1`s and update the maximum streak whenever a longer sequence is found.

# Approach

1. Initialize two variables:

   * `c` to count the current consecutive ones.
   * `max_count` to store the maximum consecutive ones found so far.
2. Traverse the array.
3. If the current element is `1`, increment `c`.
4. Otherwise, reset `c` to `0`.
5. Update `max_count` whenever `c` becomes larger.
6. Return `max_count`.

# Complexity

* Time complexity:

  * **O(n)** because we traverse the array once.

* Space complexity:

  * **O(1)** since only a few variables are used.

# Code

```python id="mb6sk7"
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c = max_count = 0

        for i in nums:
            if i != 1:
                c = 0
            else:
                c += 1

            if c > max_count:
                max_count = c

        return max_count
```
