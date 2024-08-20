class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        #Time complexity: o(n*m) equivalent to o(n), where n is no of rows and m is no of colums.
        #space Complexity: o(n*m) equivalent to o(n), due to the recursion stack. 
        oldcolor = image[sr][sc]
        newcolor = color
        if oldcolor == newcolor:
            return image

        self.dfs(image, sr, sc, oldcolor, newcolor)

        return image

    def dfs(self, image: List[List[int]], row: int, col: int, oldcolor: int, newcolor: int):
        if (row < 0 or row >= len(image) or col < 0 or col >= len(image[0]) or image[row][col] != oldcolor):
            return

        image[row][col] = newcolor

        # Recursively call dfs for the neighboring pixels
        self.dfs(image, row + 1, col, oldcolor, newcolor)
        self.dfs(image, row - 1, col, oldcolor, newcolor)
        self.dfs(image, row, col + 1, oldcolor, newcolor)
        self.dfs(image, row, col - 1, oldcolor, newcolor)
