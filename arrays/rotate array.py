# Intuition

To rotate the array to the right by `k` steps, the last `k` elements should move to the front, while the remaining elements shift to the right. We can create a new array containing the last `k` elements followed by the rest of the elements.

# Approach

1. Compute `k % len(nums)` to handle cases where `k` is larger than the array length.
2. Create an empty list `a`.
3. Add the last `k` elements of `nums` to `a`.
4. Add the remaining elements from the beginning of `nums`.
5. Copy the contents of `a` back into `nums` using `nums[:] = a`.
6. The array is modified in-place as required.

# Complexity

* Time complexity:

  * **O(n)** because every element is processed once.

* Space complexity:

  * **O(n)** because an additional array is used to store the rotated elements.

# Code

```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)

        a = []

        for i in range(len(nums) - k, len(nums)):
            a.append(nums[i])

        for j in range(len(nums) - k):
            a.append(nums[j])

        nums[:] = a
```
