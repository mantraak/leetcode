# Intuition

To determine whether `s` is a subsequence of `t`, we need to check if all characters of `s` appear in `t` in the same order. We can keep a pointer on `s` and move it forward whenever a matching character is found while traversing `t`.

# Approach

1. Initialize a pointer `i = 0` for string `s`.
2. Traverse each character in string `t`.
3. If the current character in `t` matches `s[i]`, move `i` to the next character in `s`.
4. Continue until all characters of `t` are processed.
5. If `i` reaches the length of `s`, it means all characters of `s` were found in order.
6. Return `True` if `i == len(s)`, otherwise return `False`.

# Complexity

* Time complexity:

  * **O(n)** where `n` is the length of `t`, since we traverse `t` once.

* Space complexity:

  * **O(1)** because only a pointer variable is used.

# Code

```python id="4hy0fc"
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0

        for ch in t:
            if i < len(s) and s[i] == ch:
                i += 1

        return i == len(s)
```
