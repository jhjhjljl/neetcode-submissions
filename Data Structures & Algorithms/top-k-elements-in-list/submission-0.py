"""
store occurences in hashmap, then sort by number of occurences.
time complexity: O(n log n)
space complextiy: O(n)
"""

from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for x in nums:
            counter[x] += 1
        counter_sorted = []
        for key, val in counter.items():
            counter_sorted.append([key, val])
        counter_sorted.sort(key=lambda kv: kv[1], reverse=True)
        result = []
        for i in range(k):
            result.append(counter_sorted[i][0])
        return result

        