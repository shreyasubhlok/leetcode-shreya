class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if board is None:
            return False

        squares = [set() for i in range(9)]

        for r in range(9):
            rows = set()
            cols = set()
            for c in range(9):

                if board[r][c] in rows:
                    return False
                if board[r][c]!=".":
                    rows.add(board[r][c])
                    location = 3 * (r//3) + (c//3)
                    if board[r][c] in squares[location]:
                         return False
                
                if board[r][c]!=".":
                    squares[location].add(board[r][c])
                
                if board[c][r] in cols:
                    return False
                if board[c][r]!=".":
                    cols.add(board[c][r])
                
                   
            
                

        return True
