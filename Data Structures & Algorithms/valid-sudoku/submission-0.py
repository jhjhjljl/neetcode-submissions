class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            unique = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in unique:
                    return False
                else:
                    unique.add(board[i][j])
        for i in range(9):
            unique = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                if board[j][i] in unique:
                    return False
                else:
                    unique.add(board[j][i])
        for square in range(9):
            unique = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in unique:
                        return False 
                    else:
                        unique.add(board[row][col])
        return True



