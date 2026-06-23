# Intuition

To find the third distinct maximum number, duplicate values should not be counted. A simple approach is to remove duplicates, sort the remaining numbers in descending order, and then check whether a third distinct maximum exists.

# Approach

1. Remove duplicate elements using `set(nums)`.
2. Sort the distinct elements in descending order.
3. If there are fewer than three distinct numbers, return the largest number.
4. Otherwise, return the third element in the sorted list, which represents the third maximum number.

# Complexity

* Time complexity:

  * **O(n log n)** because sorting the distinct elements dominates the runtime.

* Space complexity:

  * **O(n)** due to storing the distinct elements in a set and sorted list.

# Code

```python
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        num = sorted(set(nums), reverse=True)

        if len(num) < 3:
            return num[0]
        else:
            return num[2]
```
