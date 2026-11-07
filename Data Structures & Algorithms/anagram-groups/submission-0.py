"""
sorted_key = {
    "act": ["act", "cat"],
    "opts": ["pots", "tops", "stop"],
    "aht": ["hat"]

}
time complexity: O(klogk * n)
space complexity: O(n * k)
"""

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_keys = defaultdict(list)
        for x in strs:
            sorted_str = "".join(sorted(x))
            sorted_keys[sorted_str].append(x)
        return [li for li in sorted_keys.values()]
        