# Intuition

A palindrome reads the same forward and backward. However, the given string may contain spaces, punctuation marks, and mixed letter cases. Therefore, we first need to keep only alphanumeric characters and convert all letters to lowercase. Then we can compare the cleaned string with its reverse.

# Approach

1. Create an empty string `a`.
2. Traverse each character in the input string.
3. Check if the character is:

   * A lowercase letter (`a-z`)
   * An uppercase letter (`A-Z`)
   * A digit (`0-9`)
4. If valid, convert it to lowercase and append it to `a`.
5. After processing all characters, compare `a` with its reverse `a[::-1]`.
6. Return `True` if both are equal, otherwise return `False`.

# Complexity

* Time complexity:

  * **O(n)** because we traverse the string once and compare it with its reverse.

* Space complexity:

  * **O(n)** because a new cleaned string is created.

# Code

```python id="0pwxn3"
class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ""

        for i in s:
            if i >= 'a' and i <= 'z' or i >= 'A' and i <= 'Z' or i >= '0' and i <= '9':
                a += i.lower()

        return a == a[::-1]
```
