# Intuition
Every element in the array appears twice except for one. Using the XOR operation helps eliminate duplicate numbers because a number XOR itself equals 0, and a number XOR 0 remains unchanged.

Properties of XOR:
- `a ^ a = 0`
- `a ^ 0 = a`
- XOR is commutative and associative

By XORing all elements together, all duplicate pairs cancel out, leaving only the single number.

# Approach
1. Initialize a variable `ans` to 0.
2. Traverse the array and XOR each element with `ans`.
3. Duplicate elements cancel each other out.
4. After the loop, `ans` contains the element that appears only once.
5. Return `ans`.

# Complexity
- Time complexity:
  - **O(n)**, where `n` is the number of elements in the array.

- Space complexity:
  - **O(1)**, since only one extra variable is used.

# Code
```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0

        for num in nums:
            ans ^= num

        return ans