from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        buckets = [[] for _ in range(n)]
        counter = defaultdict(int)
        for x in nums:
            counter[x] += 1
        for key, val in counter.items():
            buckets[val - 1].append(key)
        result = []
        k_remaining = k
        for i in range(n - 1, -1, -1):
            for x in buckets[i]:
                result.append(x)
                k_remaining -= 1
                if k_remaining == 0:
                    return result
        
        