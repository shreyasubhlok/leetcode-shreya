
class Solution:
    '''
    Time= o(log(m.n))
    Space= o(1)
    '''
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        # Set up pointers to define the range of rows to search
        topRow = 0
        bottomRow = len(matrix) - 1

        #Binary search to find the potential row containing the target
        while topRow <= bottomRow:
            mid = (topRow + bottomRow) // 2

            if matrix[mid][0] < target and matrix[mid][-1] > target:  # If target is within the current row range
                break
            elif matrix[mid][0] > target:
                # If the target is smaller than the first element of mid row
                bottomRow = mid - 1
            else:
                # If the target is greater than the last element of mid row
                topRow = mid + 1

        # Set the row to search
        row = (topRow + bottomRow) // 2

        #final step- Binary search within the identified row
        left = 0
        right = len(matrix[row]) - 1

        while left <= right:
            mid = (left + right) // 2

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False


'''
[-1]: In Python, negative indexing allows you to access elements from the end of a list. Specifically, [-1] refers to the last element of the list.
so matric[0][-1] is last element of row 0. 
'''
