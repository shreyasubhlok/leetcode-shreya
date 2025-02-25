# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        # Helper function to calculate the maximum depth of the nested list
        def getMaxDepth(nestedList, depth):
            maxDepth = depth  # Track the current depth
            for element in nestedList:
                if not element.isInteger():  # If it's a nested list, go deeper
                    maxDepth = max(maxDepth, getMaxDepth(element.getList(), depth + 1))
            return maxDepth

        # Helper function to calculate the weighted sum using the max depth
        def getWeightedSum(nestedList, depth, maxDepth):
            total = 0  # Initialize the total sum for this call
            for element in nestedList:
                if element.isInteger():  # If the element is an integer
                    weight = maxDepth - depth + 1  # Calculate weight based on inverse depth
                    total += element.getInteger() * weight  # Add weighted contribution
                else:  # If the element is a nested list, recurse deeper
                    total += getWeightedSum(element.getList(), depth + 1, maxDepth)
            return total

        # Step 1: Calculate the maximum depth of the nested list
        maxDepth = getMaxDepth(nestedList, 1)

        # Step 2: Calculate the weighted sum using the calculated max depth
        return getWeightedSum(nestedList, 1, maxDepth)


    # BFS Approach for 364. Nested List Weight Sum II
    # Time Complexity: O(n), where n is the total number of elements in the nested structure
    # Space Complexity: O(d), where d is the maximum depth (due to the queue)
    def depthSumInverseBFS(nestedList: List[NestedInteger]) -> int:
        total = 0  # Final result to store the weighted sum
        currTotal = 0  # Running sum of integers encountered so far
        queue = deque(nestedList)  # Initialize the queue with the top-level list elements

        # Perform BFS level by level
        while queue:
            for _ in range(len(queue)):  # Process all elements at the current depth level
                element = queue.popleft()
                if element.isInteger():  # If the element is an integer
                    currTotal += element.getInteger()  # Add to the running total
                else:
                    # If the element is a nested list, add its contents to the queue
                    for nestedElement in element.getList():
                        queue.append(nestedElement)
            total += currTotal  # Add the running total to the final result after each level

        return total