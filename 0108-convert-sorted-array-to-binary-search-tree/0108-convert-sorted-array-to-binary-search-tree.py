# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums)==0:
            return None
        return self.isHelper(0,len(nums)-1,nums)
    
    def isHelper(self,left:int,right:int,nums:List[int])->TreeNode:
        if left>right:
            return None
        
        mid = (left+right) // 2
        
        root=TreeNode(nums[mid])
        root.left=self.isHelper(left,mid-1,nums)
        root.right=self.isHelper(mid+1,right,nums)
        
        
        return root
        