# Intuition

The problem asks us to count how many employees worked at least the target number of hours. We can simply iterate through the list and count every employee whose working hours are greater than or equal to the target.

# Approach

1. Initialize a counter `cnt` to 0.
2. Traverse through each value in the `hours` array.
3. If the current employee's hours are greater than or equal to `target`, increment the counter.
4. After checking all employees, return the counter.

# Complexity

* Time complexity:

  * **O(n)** because we traverse the array once.

* Space complexity:

  * **O(1)** since only a single counter variable is used.

# Code

```python
class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        cnt = 0

        for i in hours:
            if i >= target:
                cnt += 1

        return cnt
```
