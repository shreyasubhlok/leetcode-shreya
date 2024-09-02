class Solution:
    '''
    BFS is ideal for this problem because it ensures that the first time a 1 is reached from a 0, the shortest distance is found.

       #time complexity is O(m * n) - Each cell is processed once, and each edge (neighboring relationship) is considered once, making the BFS
        traversal take O(V + E) time. Since in a grid, the number of edges is proportional to the number of vertices, E is O(V), making the time complexity O(V).
        #space complexity is O(m * n) coz of matrix. Queue takes o(V). so total o(m*n)+o(v) = o(m*n)
    '''
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if len(mat) == 0 or len(mat[0]) == 0:
            return []
        rows = len(mat)
        cols = len(mat[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        q = []

        # Initialize the queue with all cells containing 0 and mark the rest as unvisited ('#')
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = '#'

        # Process the queue
        for currentRow, currentCol in q:
            for x, y in directions:
                new_row = currentRow + x
                new_col = currentCol + y

                # Check if the new position is within bounds and is unvisited
                if 0 <= new_row < rows and 0 <= new_col < cols and mat[new_row][new_col] == '#':
                    mat[new_row][new_col] = mat[currentRow][currentCol] + 1
                    q.append((new_row, new_col))

        return mat
