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
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        if not nestedList:
            return 0

        def helper(nestedList, depth):
            totalSum = 0
            for element in nestedList:
                if element.isInteger():  # Check if the element is an integer
                    totalSum += element.getInteger() * depth  # Multiply integer by its depth
                else:
                    totalSum += helper(element.getList(), depth + 1)  # Recurse for nested lists
            return totalSum

        # Start the recursion with depth = 1
        return helper(nestedList, 1)


    # Depth Sum Function Using BFS
    # This function computes the weighted sum of all integers in the nested list using Breadth-First Search (BFS).
    # Time Complexity: O(n), where n is the total number of elements (integers + lists)
    # Space Complexity: O(n), due to the queue used to store elements at each level
    def depthSumBFS(nestedList: List[NestedInteger]) -> int:
        if not nestedList:
            return 0
        # Initialize a queue to process elements level by level
        queue = deque()
        queue.append((nestedList, 1))  # Enqueue the initial list with depth = 1
        totalSum = 0
        while queue:
            # Dequeue the front element, which contains a list and its depth
            front = queue.popleft()
            currList = front[0]
            depth = front[1]
            for element in currList:
                if element.isInteger():  # Check if the element is an integer
                    totalSum += element.getInteger() * depth  # Add its weighted value
                else:
                    queue.append((element.getList(), depth + 1))  # Enqueue nested list with incremented depth
        return totalSum