from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)
        for x in strs:
            lookup = [0] * 26
            for c in x:
                index = ord(c) - ord("a")
                lookup[index] += 1
            mapping[tuple(lookup)].append(x)
        return list(mapping.values())