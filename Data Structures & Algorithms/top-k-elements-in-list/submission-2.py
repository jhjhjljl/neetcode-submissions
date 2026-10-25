from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]
        count = Counter(nums)
        for key, val in count.items():
            freq[val].append(key)
        result = []
        num_items = 0
        for i in range(len(freq) - 1, -1, -1):
            if num_items == k:
                break
            if not freq[i]:
                continue
            for x in freq[i]:
                result.append(x)
                num_items += 1
        return result
        