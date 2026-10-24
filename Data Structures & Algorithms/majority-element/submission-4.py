from collections import defaultdict


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        half_len = len(nums) // 2
        counter = defaultdict(int)
        for x in nums:
            counter[x] += 1
            if counter[x] > half_len:
                return x
        return None
            
