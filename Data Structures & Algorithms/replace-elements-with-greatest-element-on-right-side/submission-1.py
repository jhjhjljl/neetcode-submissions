"""
[2,4,5,3,1,2]
         i

i | temp | greatest_from_right | array
5 | 2    | 0                   | [2,4,5,3,1,0]
4 | 1    | 2                   | [2,4,5,3,2,2]
3 | 3    | 2                   | [2,4,5,2,2,2]
2 | 5    | 3                   | [2,4,3,2,2,2]
1 | 5    | 3                   | [2,4,3,2,2,2]


"""
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest_from_right = 0
        for i in range(len(arr) - 1, -1, -1):
            temp = arr[i]
            arr[i] = greatest_from_right
            greatest_from_right = max(greatest_from_right, temp)
        arr[-1] = -1
        return arr


        
        

        