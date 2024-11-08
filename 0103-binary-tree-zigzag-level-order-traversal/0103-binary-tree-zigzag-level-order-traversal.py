# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time :O(n) and space:O(n)
    def zigzagLevelOrder(self, root: TreeNode) -> list[list[int]]:
        if root == None:
            return []

        queue = deque()
        queue.append(root)
        level = 0
        res = []
        # The while loop and for loop combined only end up processing each node a single time, without repeated or redundant work. That's why o(n) and not o(n^2)
        while len(queue) != 0:
            currLevelNodes = []
            for i in range(len(queue)):
                curr = queue.popleft()
                if level % 2 == 0:
                    currLevelNodes.append(curr.val)
                else:
                    #Consider a tree level with nodes [1, 2, 3] at an odd level:
                    # If we use insert(0, curr.val) for each node, the final currLevelNodes will be [3, 2, 1], which is the reverse order.
                    currLevelNodes.insert(0, curr.val)
                if curr.left != None:
                    queue.append(curr.left)

                if curr.right != None:
                    queue.append(curr.right)
            level += 1
            res.append(currLevelNodes)
        return res