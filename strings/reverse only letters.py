# Intuition

The goal is to reverse only the letters in the string while keeping all non-letter characters in their original positions. A two-pointer approach works well by scanning from both ends and swapping only alphabetic characters.

# Approach

1. Convert the string into a list since strings are immutable in Python.
2. Initialize two pointers:

   * `left` at the beginning.
   * `right` at the end.
3. If the character at `left` is not a letter, move `left` forward.
4. If the character at `right` is not a letter, move `right` backward.
5. If both characters are letters, swap them and move both pointers.
6. Continue until the pointers meet.
7. Join the list back into a string and return it.

# Complexity

* Time complexity:

  * **O(n)** because each character is processed at most once.

* Space complexity:

  * **O(n)** because the string is converted into a list.

# Code

```python id="8l8f3k"
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        left, right = 0, len(s) - 1

        while left < right:
            if not s[left].isalpha():
                left += 1
            elif not s[right].isalpha():
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        return "".join(s)
```
