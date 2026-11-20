class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n_rows = len(matrix)
        n_cols = len(matrix[0])
        left = 0
        right = n_rows * n_cols - 1 
        while left <= right:
            mid = (left + right) // 2
            row = mid // n_cols 
            col = mid % n_cols
            if target > matrix[row][col]:
                left = mid + 1
            elif target < matrix[row][col]:
                right = mid - 1
            else:
                return True
        return False


        
        