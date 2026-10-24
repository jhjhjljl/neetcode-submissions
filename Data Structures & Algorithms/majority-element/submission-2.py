from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        counts = Counter(nums)
        for k, v in counts.items():
            if v > (n // 2):
                return k
