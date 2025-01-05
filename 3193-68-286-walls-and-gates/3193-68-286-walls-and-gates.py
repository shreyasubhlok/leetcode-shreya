class Solution:
    #Time and space: O(r*c)
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        Modify the given 2D grid 'rooms' in-place to fill each empty room with
        the distance to its nearest gate. A value of 0 represents a gate, -1 represents
        a wall, and 2147483647 represents an empty room.
        """
        # Get the number of rows and columns in the grid
        rows = len(rooms)
        cols = len(rooms[0])

        # Initialize a queue to perform BFS
        q = deque()

        # Define the constant representing an empty room
        inf = 2147483647


        # Directions array to explore the four possible moves (up, down, left, right)
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # Step 1: Find all gates (value 0) and add their positions to the queue
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    q.append((r, c))
        
        # Step 2: Perform BFS from each gate
        while q:
            # Pop the front element from the queue (current position)
            currentRow, currentCol = q.popleft()
            # Explore all four directions from the current position
            for x, y in directions:
                newRow = currentRow + x
                newCol = currentCol + y
                 # Check if the new position is within grid bounds
                # and if it's an empty room (unvisited)
                if ( 0 <= newRow < rows and 0 <= newCol < cols and rooms[newRow][newCol] == inf):
                    # Update the empty room with the distance from the nearest gate
                    rooms[newRow][newCol] = rooms[currentRow][currentCol] + 1
                    q.append((newRow, newCol))  # Add the new position to the queue for further exploration
                   
