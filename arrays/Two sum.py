# Intuition
The problem asks us to find two numbers in the array whose sum equals the target and return their indices. Since every possible pair could potentially form the target sum, a straightforward approach is to check all pairs until a valid one is found.

# Approach
Use two nested loops:

1. Select the first element using the outer loop.
2. For each selected element, check all elements after it using the inner loop.
3. If the sum of the two elements equals the target, return their indices immediately.
4. Since the problem guarantees exactly one solution, the function will always find and return a valid pair.

# Complexity
- Time complexity:
  - **O(n²)** because every pair of elements may need to be checked.

- Space complexity:
  - **O(1)** since no extra data structure is used.

# Code
```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
