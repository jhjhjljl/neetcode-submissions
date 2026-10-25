from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]
        count = Counter(nums)
        for key, val in count.items():
            freq[val].append(key)
        result = []
        for i in range(len(freq) - 1, -1, -1):
            for x in freq[i]:
                result.append(x)
                if len(result) == k:
                    return result
        return result
        