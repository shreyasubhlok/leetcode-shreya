class Solution:
    # time is o(m*n), m rows and n cols
    # space is o(m*n) worst case
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        # Edge case: if the grid is empty, return 0
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        uniqueIsland = set()  # Set to store unique island shapes

        # DFS function to explore each island and record its relative shape
        def traversedfs(r, c, orignal_r, orignal_c, shape):
            # Check if the cell is out of bounds or water (0)
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0:
                return

            grid[r][c] = 0  # Mark the cell as visited by setting it to 0

            # Record the relative position from the starting cell
            shape.append((r - orignal_r, c - orignal_c))

            # Explore in all four directions (down, up, right, left)
            traversedfs(r + 1, c, orignal_r, orignal_c, shape)  # down
            traversedfs(r - 1, c, orignal_r, orignal_c, shape)  # up
            traversedfs(r, c + 1, orignal_r, orignal_c, shape)  # right
            traversedfs(r, c - 1, orignal_r, orignal_c, shape)  # left

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # Start DFS if we find an unvisited land cell (1)
                if grid[i][j] == 1:
                    shape = []  # Initialize a list to record the shape of the island
                    # Use (i, j) as the base point
                    # Convert shape to tuple and add to the set of unique shapes
                    traversedfs(i, j, i, j, shape)
                    uniqueIsland.add(tuple(shape))

        return len(uniqueIsland)
