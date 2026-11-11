"""
nums = [1,2,1,0,4,2,6], k = 3

[1,4,2,3,4,2,6]
 l
     r

l | r | queue (indexes)     | result (indexes, convert later)
0 | 0 | [0]                 |
0 | 1 | [1]                 | 
0 | 2 | [1, 2]              | [1]
1 | 3 | [1, 3]              | [1, 1]
2 | 4 | [4]                 | [1, 1, 4]
3 | 5 | [4, 6]              | [1, 1, 4, 4]        
4 | 6 | [6]                 | [1, 1, 4, 4, 6]

[1, 1, 4, 4, 6]
[4, 4, 4, 4, 6]

- remove stale index from the window
- pop from right until your standing number is in order
- append to result when the window is completed.

time: O(n)
space: O(k)
"""

from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        l = 0
        q = deque()
        result = []
        for r in range(n):
            if q and q[0] < l:
                q.popleft()
            while q and nums[q[-1]] < nums[r]:
                q.pop() 
            q.append(r)
            if r >= k - 1:
                result.append(nums[q[0]])
                l += 1
        return result
            


        