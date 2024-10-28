class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        maxLeft=0
        maxRight=0
        ans=0
        while left<=right:
            if height[left]<=height[right]:
                maxLeft=max(maxLeft,height[left])
                ans=ans+maxLeft-height[left]
                left=left+1
            else:
                maxRight=max(maxRight,height[right])
                ans=ans+maxRight-height[right]
                right=right-1
        return ans