class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        for chars in zip(*strs):
            if len(set(chars)) != 1:
                return result
            else:
                result += chars[0]
        return result
