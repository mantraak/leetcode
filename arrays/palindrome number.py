# Intuition
A palindrome number reads the same forward and backward. To check this, we can reverse the digits of the number and compare the reversed number with the original number. If both are equal, the number is a palindrome.

# Approach
1. Store the original number in a temporary variable.
2. Initialize `rev` to 0 to build the reversed number.
3. Extract the last digit using the modulo operator (`% 10`).
4. Append the digit to `rev`.
5. Remove the last digit from the number using integer division (`// 10`).
6. Repeat until all digits are processed.
7. Compare the reversed number with the original number.
   - If they are equal, return `True`.
   - Otherwise, return `False`.

# Complexity
- Time complexity:
  - **O(log₁₀ n)**, since we process each digit once.

- Space complexity:
  - **O(1)**, as only a few variables are used.

# Code
```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0
        temp = x

        while temp > 0:
            t = temp % 10
            rev = (rev * 10) + t
            temp = temp // 10

        if rev == x:
            return True
        else:
            return False