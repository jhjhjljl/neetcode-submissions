"""
[-1, 0, 1, 2, -1, -4]

[-4, -1, -1, 0, 1, 2]
             i  l  r

-4 -1 2 = -3 < 0 move left
-4 -1 2 skip left 
-4 -1 0 = -5 < 0 move left
-4  1 2 = -1 < 0 move left
-1 -1 2 = 0 move left and right
-1  0 1 = 0
-1  0 1 skip i
 0  1 1 = 2
 done

time: O(n^2)
space: O(1)
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = n - 1
            while l < r:
                if (l > i + 1) and (nums[l] == nums[l - 1]):
                    l += 1
                    continue
                if (r < n - 1) and (nums[r] == nums[r + 1]):
                    r -= 1
                    continue
                current_sum = nums[i] + nums[l] + nums[r]
                if current_sum > 0:
                    r -= 1
                elif current_sum < 0:
                    l += 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
        return result


        