# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        result=[]
        def getHeight(node):
            if node is None:
                return -1
            leftHeight=getHeight(node.left)
            rightHeight=getHeight(node.right)
            level=max(leftHeight,rightHeight)+1
            
            if level==len(result):
                result.append([])
            result[level].append(node.val)
            return level
        
        getHeight(root)
        return result