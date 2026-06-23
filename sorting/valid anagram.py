# Intuition

Two strings are anagrams if they contain the same characters with the same frequencies. We can count the occurrences of each character in the first string and then decrease those counts using the second string. If every count matches perfectly, the strings are anagrams.

# Approach

1. If the lengths of the two strings are different, return `False`.
2. Create a dictionary `freq` to store character frequencies from `s`.
3. Traverse `s` and increment the count of each character.
4. Traverse `t`:

   * If a character is not present in `freq`, return `False`.
   * Decrement its count.
   * If the count becomes negative, return `False`.
5. If all checks pass, return `True`.

# Complexity

* Time complexity:

  * **O(n)** where `n` is the length of the strings.

* Space complexity:

  * **O(k)** where `k` is the number of distinct characters.

# Code

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        for ch in t:
            if ch not in freq:
                return False

            freq[ch] -= 1

            if freq[ch] < 0:
                return False

        return True
```
