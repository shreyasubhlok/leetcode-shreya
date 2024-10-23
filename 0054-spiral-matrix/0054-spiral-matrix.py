class Solution:
    # Time is o(m*n)
    # space is o(1)
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if len(matrix) == 0:
            return res

        # Define the boundaries of the matrix
        row_begin = 0
        row_end = len(matrix) - 1
        col_begin = 0
        col_end = len(matrix[0]) - 1

        # Continue the loop while boundaries are valid
        while row_begin <= row_end and col_begin <= col_end:
            # Traverse from left to right along the top row
            for i in range(col_begin, col_end + 1):
                res.append(matrix[row_begin][i])
            row_begin = row_begin + 1

            # Traverse from top to bottom along the right column
            for i in range(row_begin, row_end + 1):
                res.append(matrix[i][col_end])
            col_end = col_end - 1

            # Traverse from right to left along the bottom row (if still in bounds)
            if row_begin <= row_end:
                for i in range(col_end, col_begin - 1, -1):
                    res.append(matrix[row_end][i])
                row_end = row_end - 1

            # Traverse from bottom to top along the left column (if still in bounds)
            if col_begin <= col_end:
                for i in range(row_end, row_begin - 1, -1):
                    res.append(matrix[i][col_begin])
                col_begin = col_begin + 1

        return res


"""
for i in range(row_end, row_begin - 1, -1): -> 
range(start, stop, step): This generates a sequence of numbers from start to stop - 1, moving by step.
In this specific case:
row_end: The loop starts at the row_end (the last row).
row_begin - 1: The loop stops before row_begin. By subtracting 1 from row_begin, it ensures that row_begin itself is included in the loop (since the range() function is exclusive of the stop value).
-1: The step is -1, which means the loop iterates in reverse, decrementing by 1 each time.

"""
