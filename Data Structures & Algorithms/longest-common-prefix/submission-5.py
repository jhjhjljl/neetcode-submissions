class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        base = strs[0]
        for i, c in enumerate(base):
            for s in strs:
                if i == len(s) or c != s[i]:
                    return base[:i]
        return base