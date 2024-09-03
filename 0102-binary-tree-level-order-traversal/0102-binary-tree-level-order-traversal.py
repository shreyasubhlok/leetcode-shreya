# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #Time complexity: o(n)
    #space complexity: o(n)
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return None

        resList = []
        queue = deque([root])    # Use a deque for efficient queue operations.

        # Continue processing until the queue is empty
        while len(queue) > 0:
            ans = []  # List to hold values of nodes at the current leve
            levelSize = len(queue)   # Number of nodes at the current level

            # Iterate over all nodes at the current level
            for l in range(levelSize):
                node = queue.popleft()   # Dequeue a node from the front of the queue
                ans.append(node.val) # Add the value of the current node to the ans list

                # Enqueue the left child if it exists
                if node.left != None:
                    queue.append(node.left)

                # Enqueue the right child if it exists
                if node.right != None:
                    queue.append(node.right)

            resList.append(ans) # Add the list of node values at the current level to the result list


        return resList
    
'''
using a deque (queue = deque()) vs Using a List (queue = [])
The deque (double-ended queue) is optimized for efficient appending and popping from both ends.
append() and popleft() operations both have O(1) time complexity.

Using lists for queue operations can be inefficient. 
Specifically, the pop(0) operation (to dequeue) has O(n) time complexity because it requires shifting all the elements in the list.

So better to use queue =dequeue() here.

'''