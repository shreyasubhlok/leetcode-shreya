class Solution:
    # time: o(1), coz, O(n*m)=O(9*9), O(81) ...it will laways be 9*9
    # space: o(1), coz, O(n*m)=O(9*9), O(81) ...it will laways be 9*9
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if board is None:
            return False

        # Initialize list of sets for rows, columns, and 3x3 squares to track seen numbers
        rows = [set() for i in range(9)]  # rows = [set(), set(), set(), set(), set(), set(), set(), set(), set()]
        cols = [set() for i in range(9)]  # cols = [set(), set(), set(), set(), set(), set(), set(), set(), set()]
        squares = [set() for i in range(9)]  # squares = [set(), set(), set(), set(), set(), set(), set(), set(), set()]

        # Iterate through each cell in the 9x9 board
        for r in range(9):
            for c in range(9):
                # Skip empty cells represented by "."
                if board[r][c] == ".":
                    continue

                # Check for duplicates in the current row
                if board[r][c] in rows[r]:
                    return False
                rows[r].add(board[r][c])  # Add current number to the row set

                # Check for duplicates in the current column
                if board[r][c] in cols[c]:
                    return False
                cols[c].add(board[r][c])  # Add current number to the column set

                location = 3 * (r // 3) + (c // 3)  # Calculate the index of the 3x3 square (0 to 8)
                # Check for duplicates in the current 3x3 square
                if board[r][c] in squares[location]:
                    return False
                squares[location].add(board[r][c])  # Add current number to the 3x3 square set

        return True