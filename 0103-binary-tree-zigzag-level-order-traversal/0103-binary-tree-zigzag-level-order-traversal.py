# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> list[list[int]]:
        if root == None:
            return []

        queue = deque()
        queue.append(root)
        level = 0
        res = []
        while len(queue) != 0:
            currLevelNodes = []
            for i in range(len(queue)):
                curr = queue.popleft()
                if level % 2 == 0:
                    currLevelNodes.append(curr.val)
                else:
                    currLevelNodes.insert(0, curr.val)
                if curr.left != None:
                    queue.append(curr.left)

                if curr.right != None:
                    queue.append(curr.right)
            level+=1
            res.append(currLevelNodes)
        return res