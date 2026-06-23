# Intuition

The array may contain negative numbers, and squaring them can change their order. A simple approach is to square every element and then sort the resulting array.

# Approach

1. Create an empty list `a`.
2. Traverse through the array.
3. Square each element and append it to `a`.
4. Sort the list `a`.
5. Return the sorted list.

# Complexity

* Time complexity:

  * **O(n log n)** because sorting dominates the runtime.

* Space complexity:

  * **O(n)** since a new array is created to store the squared values.

# Code

```python id="4w3r7a"
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        a = []

        for i in range(len(nums)):
            a.append(nums[i] ** 2)

        return sorted(a)
```
