from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for x in strs:
            mapping = [0] * 26
            for c in x:
                mapping[ord(c) - ord("a")] += 1
            anagrams[tuple(mapping)].append(x)
        return list(anagrams.values())
        