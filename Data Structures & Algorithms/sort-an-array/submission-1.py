class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.split(nums)
    
    def merge(self, left, right):
        i = j = 0
        res = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        res += left[i:]
        res += right[j:]
        return res
        
    
    def split(self, nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = self.split(nums[:mid])
        right = self.split(nums[mid:])
        return self.merge(left, right)
