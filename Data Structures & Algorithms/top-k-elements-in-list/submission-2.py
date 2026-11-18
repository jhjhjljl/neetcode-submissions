from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        buckets = [[] for _ in range(n)]
        counter = Counter(nums)
        for key, val in counter.items():
            buckets[val - 1].append(key)
        result = []
        for i in range(n - 1, -1, -1):
            for x in buckets[i]:
                result.append(x)
                if len(result) == k:
                    return result
        return result

            
        
        