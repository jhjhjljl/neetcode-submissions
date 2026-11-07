"""
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


act
[1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]

{
    "10100...1000": ["act"]
}

time complexity: O(n*k)
space complexitiy: O(n*k)
where n is the number of strings and k is the length of string.
"""

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for x in strs:
            char_count = [0] * 26
            for c in x:
                char_index = ord(c) - ord("a")
                char_count[char_index] += 1
            groups[tuple(char_count)].append(x)
        return list(groups.values())
        