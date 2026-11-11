"""
nums = [3, 1, 4, 1, 5], k = 3

[3, 1, 4, 1, 5]
       l
             r

l | r | q      | max_num
0 | 0 | [0]
0 | 1 | [0, 1]
0 | 2 | [2]
1 | 3 | [2, 3]
2 | 4 | [4]



nums = [5, 1, 3] k = 2.
[5, 1, 3]
    l
       r

l | r | q      | max_num
0 | 0 | [5]    | 
0 | 1 | [5, 1] | 5
1 | 2 | [3]    | 3

"""

from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        result = []
        for r in range(len(nums)):
            if q and q[0] < r - k + 1:
                q.popleft()
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            if r >= k - 1:
                result.append(nums[q[0]])
        return result

            


        