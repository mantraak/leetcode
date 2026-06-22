# Intuition
To determine whether an array contains duplicate elements, we need a way to quickly check if a number has already been seen before. A hash set provides **O(1)** average-time lookup and insertion, making it ideal for this task.

# Approach
1. Create an empty hash set called `seen`.
2. Traverse each element in the array.
3. If the current element is already present in the hash set, a duplicate exists, so return `True`.
4. Otherwise, add the element to the hash set.
5. If the traversal completes without finding any duplicate, return `False`.

# Complexity
- Time complexity:
  - **O(n)**, where `n` is the number of elements in the array. Each lookup and insertion in the hash set takes O(1) on average.

- Space complexity:
  - **O(n)**, as the hash set may store up to all unique elements in the array.

# Code
```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False