class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        result = [0] * n
        for i in range(n):
            max_num = 0
            for j in range(i + 1, n):
                max_num = max(max_num, arr[j])
            result[i] = max_num
        result[-1] = -1
        return result

            
        