# Intuition

The string needs to be reversed in-place without using extra space. A two-pointer approach works well by swapping characters from the beginning and end of the array until both pointers meet.

# Approach

1. Initialize two pointers:

   * `i` at the start of the array.
   * `j` at the end of the array.
2. While `i <= j`:

   * Swap the characters at positions `i` and `j`.
   * Move `i` one step forward.
   * Move `j` one step backward.
3. Continue until the pointers meet or cross each other.
4. The array is modified in-place and becomes reversed.

# Complexity

* Time complexity:

  * **O(n)** because each element is visited at most once.

* Space complexity:

  * **O(1)** since the reversal is done in-place without using extra storage.

# Code

```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s) - 1

        while i <= j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

        return s
```
