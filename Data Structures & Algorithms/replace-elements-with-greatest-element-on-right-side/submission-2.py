"""
[2,4,5,3,1,2]
   i

i | right_max | ans 
5 | 2         | [0,0,0,0,0,-1] 
4 | 2         | [0,0,0,0,2,-1] 
3 | 3         | [0,0,0,2,2,-1] 
2 | 5         | [0,0,3,2,2,-1] 
1 | 5         | [0,5,3,2,2,-1] 
0 | 5         | [0,5,3,2,2,-1] 
"""
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        right_max = -1
        result = [0] * n
        for i in range(n - 1, -1, -1):
            result[i] = right_max
            right_max = max(right_max, arr[i])
        return result
            


        
        

        