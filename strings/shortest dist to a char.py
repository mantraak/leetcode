# Intuition

For each position in the string, we need the distance to the nearest occurrence of the target character. A single scan cannot always find the closest occurrence because a nearer target character may exist on the other side. Therefore, we perform two passes:

1. Left to right to find the nearest occurrence on the left.
2. Right to left to find the nearest occurrence on the right.

The minimum of these two distances gives the answer.

# Approach

1. Create an array `ans` to store distances.
2. Traverse from left to right:

   * Keep track of the most recent occurrence of `c`.
   * Store the distance from the current index to that occurrence.
3. Traverse from right to left:

   * Keep track of the nearest occurrence of `c` on the right.
   * Update each position with the smaller of the existing distance and the right-side distance.
4. Return the resulting array.

# Complexity

* Time complexity:

  * **O(n)** because the string is traversed twice.

* Space complexity:

  * **O(n)** for the answer array.

# Code

```python
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        ans = [0] * n

        prev = float('-inf')
        for i in range(n):
            if s[i] == c:
                prev = i
            ans[i] = i - prev

        prev = float('inf')
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i
            ans[i] = min(ans[i], prev - i)

        return ans
```
