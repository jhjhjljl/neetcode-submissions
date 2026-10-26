class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        length = len(nums)
        nums.sort()
        for i in range(length):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = length - 1
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return result
                



        