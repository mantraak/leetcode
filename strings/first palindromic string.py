# Intuition

A palindrome reads the same forward and backward. We can check each word one by one and return the first word that is equal to its reverse.

# Approach

1. Traverse through each word in the array.
2. Reverse the current word using slicing `[::-1]`.
3. Compare the word with its reversed version.
4. If both are equal, return the word immediately.
5. If no palindrome is found, return an empty string.

# Complexity

* Time complexity:

  * **O(n × m)** where `n` is the number of words and `m` is the average length of a word.

* Space complexity:

  * **O(m)** because a reversed copy of a word is created.

# Code

```python id="9l2xmr"
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        a = ""

        for i in range(len(words)):
            n = words[i][::-1]

            if words[i] == n:
                a += words[i]
                break

        return a
```
