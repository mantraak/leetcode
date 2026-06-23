# Intuition

The majority element appears more than ⌊n / 2⌋ times. Instead of counting the frequency of every element, we can use the Boyer-Moore Voting Algorithm. The idea is that the majority element can cancel out all other elements and still remain as the final candidate.

# Approach

1. Initialize:

   * `count = 0`
   * `candidate = None`
2. Traverse through the array.
3. If `count` becomes 0, choose the current element as the new candidate.
4. If the current element equals the candidate, increment `count`.
5. Otherwise, decrement `count`.
6. After the traversal, the candidate will be the majority element.
7. Return the candidate.

# Complexity

* Time complexity:

  * **O(n)** because the array is traversed once.

* Space complexity:

  * **O(1)** since only two variables are used.

# Code

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate
```
