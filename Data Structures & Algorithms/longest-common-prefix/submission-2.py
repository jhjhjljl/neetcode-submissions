class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        base = strs[0]
        prefix = 0

        for i in range(len(base)):
            same = True
            for s in strs[1:]:
                if base[i] != s[i]:
                    same = False
            if same:
                prefix += 1
            else:
                break
        
        return base[:prefix]
        