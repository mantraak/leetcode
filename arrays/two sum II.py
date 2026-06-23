# Intuition

Since the array is already sorted, we can use two pointers instead of checking every pair. If the current sum is smaller than the target, we need a larger value, so we move the left pointer forward. If the sum is larger than the target, we need a smaller value, so we move the right pointer backward.

# Approach

1. Initialize two pointers:

   * `left` at the beginning of the array.
   * `right` at the end of the array.
2. Calculate the sum of the elements at both pointers.
3. If the sum equals the target, return their 1-based indices.
4. If the sum is smaller than the target, move `left` one step forward.
5. If the sum is larger than the target, move `right` one step backward.
6. Continue until the pair is found.

# Complexity

* Time complexity:

  * **O(n)** because each pointer moves at most `n` times.

* Space complexity:

  * **O(1)** since no extra data structure is used.

# Code

```python id="v1z5jq"
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
```
