class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        base = strs[0]
        prefix = 0 

        for i in range(len(base)):
            same = True
            for s in strs[1:]:
                try:
                    if s[i] != base[i]:
                        same = False 
                except IndexError:
                    same = False
                    break
            if same:
                prefix += 1
            else:
                break
        
        return base[:prefix] 
            

        
