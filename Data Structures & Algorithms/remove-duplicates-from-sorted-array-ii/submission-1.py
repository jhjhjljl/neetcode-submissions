"""
[2,10,10,30,30,30]
             l
                r
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counts = {
            nums[0]: 1
        }
        left = 0
        for right in range(1, len(nums)):
            if nums[right] not in counts:
                left += 1
                counts[nums[right]] = 1
                nums[left] = nums[right]
            else:
                if counts[nums[right]] < 2:
                    left += 1
                    nums[left] = nums[right]
                    counts[nums[right]] += 1
        return left + 1


        