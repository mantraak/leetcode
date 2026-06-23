# Intuition

Since `nums1` already has enough space to hold all elements from both arrays, we can merge them from the end. By comparing the largest remaining elements in both arrays and placing the larger one at the last available position, we avoid overwriting useful values in `nums1`.

# Approach

1. Initialize three pointers:

   * `i` at the last valid element of `nums1` (`m - 1`).
   * `j` at the last element of `nums2` (`n - 1`).
   * `k` at the last position of `nums1` (`m + n - 1`).
2. While there are elements remaining in `nums2`:

   * If `nums1[i]` is larger, place it at position `k`.
   * Otherwise, place `nums2[j]` at position `k`.
3. Move the corresponding pointers after each placement.
4. Continue until all elements of `nums2` are merged into `nums1`.

# Complexity

* Time complexity:

  * **O(m + n)** because each element is processed at most once.

* Space complexity:

  * **O(1)** since the merge is performed in-place.

# Code

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1
        j = n - 1
        k = m + n - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1

            k -= 1
```
