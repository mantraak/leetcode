# Intuition

Only the vowels in the string need to be reversed while keeping all other characters in their original positions. A two-pointer approach can efficiently find vowels from both ends and swap them.

# Approach

1. Convert the string into a list because strings are immutable in Python.
2. Initialize two pointers:

   * `i` at the beginning of the string.
   * `j` at the end of the string.
3. Move `i` forward until a vowel is found.
4. Move `j` backward until a vowel is found.
5. When both pointers point to vowels, swap them.
6. Continue until the pointers meet or cross.
7. Join the list back into a string and return it.

# Complexity

* Time complexity:

  * **O(n)** because each character is visited at most once.

* Space complexity:

  * **O(n)** because the string is converted into a list.

# Code

```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        i, j = 0, len(s) - 1
        s = list(s)

        while i < j:
            if s[i] not in 'aeiouAEIOU':
                i += 1
            elif s[j] not in 'aeiouAEIOU':
                j -= 1
            elif s[i] in 'aeiouAEIOU' and s[j] in 'aeiouAEIOU':
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        return "".join(s)
```
