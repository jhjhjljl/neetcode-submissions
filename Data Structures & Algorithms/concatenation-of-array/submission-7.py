"""
n = 4

0 % 3
"""
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (n * 2) 
        for i in range(n * 2):
            index = i % n
            print(index)
            ans[i] = nums[index]
        return ans
        