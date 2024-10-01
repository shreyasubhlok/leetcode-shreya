from typing import List
from collections import deque


class Solution:
    # multi source BFS algorithm
    # time = o(n*m), n rows and m colums
    # space: o(n*m), due to the space used by the queue
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0
        time = 0  # Track the number of minutes taken
        queue = deque()  # Queue to store rotten oranges for multi-source BFS
        noOfFreshOranges = 0  # Counter for fresh oranges
        rows = len(grid)  # Number of rows in the grid
        cols = len(grid[0])  # Number of columns in the grid

        # Step 1: Initialize the queue and count the fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:  # Fresh orange
                    noOfFreshOranges += 1
                if grid[r][c] == 2:  # Rotten orange
                    queue.append([r, c])

        # Directions for adjacent cells (right, left, down, up)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        # Step 2: Perform BFS to rot adjacent fresh oranges
        while len(queue) != 0 and noOfFreshOranges > 0:
            # Process all rotten oranges in the current level
            for i in range(len(queue)):
                temp = queue.popleft()  # Get the current rotten orange position
                row = temp[0]
                col = temp[1]
                # Explore all adjacent cells
                for dr, dc in directions:
                    newRow = row + dr
                    newCol = col + dc
                    # If the new position is out of bounds or not a fresh orange, continue
                    if newRow < 0 or newRow >= len(grid) or newCol < 0 or newCol >= len(grid[0]) or grid[newRow][newCol] != 1:
                        continue
                    # Mark the fresh orange as rotten
                    grid[newRow][newCol] = 2
                    queue.append([newRow, newCol])  # Add the new rotten orange to the queue
                    noOfFreshOranges -= 1  # Decrease the count of fresh oranges

            time = time + 1  # Increase the time taken by 1 minute after each level of BFS

        # Step 3: If there are no fresh oranges left, return the time taken, otherwise return -1
        if noOfFreshOranges == 0:
            return time
        else:
            return -1



