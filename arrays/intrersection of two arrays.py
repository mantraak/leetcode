# Intuition

The intersection of two arrays contains only the unique elements that appear in both arrays. Since sets automatically remove duplicates and provide efficient lookup operations, converting both arrays into sets makes finding common elements straightforward.

# Approach

1. Convert `nums1` and `nums2` into sets to remove duplicate values.
2. Use the `intersection()` method to find elements present in both sets.
3. Convert the resulting set back into a list.
4. Return the list of common unique elements.

# Complexity

* Time complexity:

  * **O(n + m)** where `n` and `m` are the lengths of the two arrays. Creating sets and finding the intersection are linear operations.

* Space complexity:

  * **O(n + m)** for storing the elements in two sets.

# Code

```python id="5b9x1r"
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1, n2 = set(nums1), set(nums2)
        return list(n1.intersection(n2))
```
