# Intuition

The problem asks us to count how many numbers in the array contain an even number of digits. A simple way to determine the number of digits in a number is to convert it into a string and check its length.

# Approach

1. Initialize a counter `c` to keep track of numbers with an even number of digits.
2. Traverse through each number in the array.
3. Convert the number to a string using `str()`.
4. Check if the length of the string is even using `len(str(i)) % 2 == 0`.
5. If true, increment the counter.
6. Return the final count.

# Complexity

* Time complexity:

  * **O(n × d)** where `n` is the number of elements and `d` is the number of digits in each number. Since digit length is small, it is effectively **O(n)**.

* Space complexity:

  * **O(1)** ignoring the temporary string conversion.

# Code

```python
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        c = 0

        for i in nums:
            if len(str(i)) % 2 == 0:
                c += 1

        return c
```
