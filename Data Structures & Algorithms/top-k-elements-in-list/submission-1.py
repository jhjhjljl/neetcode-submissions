from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        sorted_count = []
        for key, val in count.items():
            sorted_count.append([val, key])
        sorted_count.sort()
        result = []
        current = 0
        for i in range(len(sorted_count) - 1, -1, -1):
            if current == k:
                break
            result.append(sorted_count[i][1])
            current += 1
        return result
            

        