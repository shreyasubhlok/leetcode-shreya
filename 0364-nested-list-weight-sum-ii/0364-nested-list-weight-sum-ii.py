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