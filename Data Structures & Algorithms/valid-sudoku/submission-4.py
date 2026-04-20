class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_seen = {}
        col_seen = {}
        square_seen = {} 
        for i in range(9):
            for j in range(9):
                row = i//3
                col = j//3
                if board[i][j] in square_seen.get((row,col),[]):
                    return False
                if board[i][j] in row_seen.get(j,[]):
                    return False
                if board[j][i] in col_seen.get(j,[]):
                    return False
                if board[i][j] != '.':
                    row_seen.setdefault(j,[]).append(board[i][j])
                if board[j][i] != '.':
                    col_seen.setdefault(j,[]).append(board[j][i])
                if board[i][j] != '.':
                    square_seen.setdefault((row,col),[]).append(board[i][j])
        return True
