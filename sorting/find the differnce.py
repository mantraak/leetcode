# Intuition

String `t` is formed by shuffling string `s` and adding one extra character. If we XOR all characters from both strings together, every matching character will cancel out, leaving only the extra character.

# Approach

1. Initialize a variable `result = 0`.
2. Traverse through string `s` and XOR the ASCII value of each character with `result`.
3. Traverse through string `t` and XOR the ASCII value of each character with `result`.
4. Matching characters cancel each other out because:

   * `a ^ a = 0`
   * `0 ^ b = b`
5. After processing both strings, `result` contains the ASCII value of the extra character.
6. Convert it back to a character using `chr()` and return it.

# Complexity

* Time complexity:

  * **O(n)** where `n` is the length of the strings.

* Space complexity:

  * **O(1)** since only one variable is used.

# Code

```python id="v2x7mj"
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = 0

        for ch in s:
            result ^= ord(ch)

        for ch in t:
            result ^= ord(ch)

        return chr(result)
```
