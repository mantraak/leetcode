# Intuition

The goal is to combine two strings by taking characters alternately from each string. We can iterate through both strings simultaneously and append one character from each string at a time. After one string is exhausted, append the remaining part of the longer string.

# Approach

1. Create an empty list `res` to store the merged characters.
2. Find the length of the shorter string using `min(len(word1), len(word2))`.
3. Traverse both strings up to this length.
4. Append one character from `word1` and then one from `word2`.
5. After the loop, append any remaining characters from either string.
6. Join the list into a string and return it.

# Complexity

* Time complexity:

  * **O(n + m)** where `n` and `m` are the lengths of the two strings.

* Space complexity:

  * **O(n + m)** because the result string stores all characters from both strings.

# Code

```python id="l2x7mf"
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        n = min(len(word1), len(word2))

        for i in range(n):
            res.append(word1[i])
            res.append(word2[i])

        res.append(word1[n:])
        res.append(word2[n:])

        return "".join(res)
```
