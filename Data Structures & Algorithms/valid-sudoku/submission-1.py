class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for row in range(9):
            for col in range(9):
                value = board[row][col]
                if value == ".":
                    continue
                if (value, 0, row) in seen or \
                (value, 1, col) in seen or \
                (value, 2, row // 3, col // 3) in seen:
                    return False
                seen.add((value, 0, row))
                seen.add((value, 1, col))
                seen.add((value, 2, row // 3, col // 3))
        return True




        