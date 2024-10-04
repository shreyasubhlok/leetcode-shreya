class Solution:
    def maxArea(self, height: List[int]) -> int:
        start=0
        end=len(height)-1
        maximumArea=0
        while start<end:
            width=end-start
            currentHeight=min(height[start],height[end])
            area=width*currentHeight
            maximumArea=max(area,maximumArea)
            if height[start]<height[end]:
                start+=1
            else:
                end-=1
        
        return maximumArea
            