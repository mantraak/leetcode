# Intuition

The running sum at any index is the sum of all elements from the beginning of the array up to that index. By keeping track of a cumulative total while traversing the array, we can efficiently build the running sum array.

# Approach

Use a single loop:

1. Initialize a variable `total` to store the cumulative sum.
2. Create an empty list `arr` to store the running sums.
3. Traverse through each element in `nums`.
4. Add the current element to `total`.
5. Append `total` to `arr`.
6. After processing all elements, return `arr`.

# Complexity

* Time complexity:

  * **O(n)** because we traverse the array only once.

* Space complexity:

  * **O(n)** since we store the running sums in a separate list.

# Code

```python
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total = 0
        arr = []

        for n in nums:
            total += n
            arr.append(total)

        return arr
```
