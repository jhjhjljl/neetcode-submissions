class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seen = set()
            for j in range(9):
                current_item = board[i][j]
                if current_item == ".":
                    continue
                if current_item in seen:
                    return False
                seen.add(current_item)
        for i in range(9):
            seen = set()
            for j in range(9):
                current_item = board[j][i]
                if current_item == ".":
                    continue
                if current_item in seen:
                    return False
                seen.add(current_item)
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row_index = (square // 3) * 3 + i
                    col_index = (square % 3) * 3 + j
                    current_item = board[row_index][col_index]
                    if current_item == ".":
                        continue
                    if current_item in seen:
                        return False
                    seen.add(current_item)
        return True

        

        