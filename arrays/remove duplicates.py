# Intuition

Since the array is already sorted, duplicate elements will always be adjacent. We can use two pointers: one pointer keeps track of the last unique element, while the other scans through the array. Whenever a new unique element is found, place it next to the previous unique element.

# Approach

1. Handle the edge case where the array is empty.
2. Initialize pointer `j = 0` to track the position of the last unique element.
3. Traverse the array from index `1`.
4. If the current element is different from `nums[j]`:

   * Move `j` forward.
   * Copy the current element to `nums[j]`.
5. After the traversal, the first `j + 1` elements contain all unique values.
6. Return `j + 1` as the number of unique elements.

# Complexity

* Time complexity:

  * **O(n)** because the array is traversed once.

* Space complexity:

  * **O(1)** since the modification is done in-place.

# Code

```python id="j8c3lw"
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        j = 0

        for i in range(1, len(nums)):
            if nums[j] != nums[i]:
                j += 1
                nums[j] = nums[i]

        return j + 1
```
