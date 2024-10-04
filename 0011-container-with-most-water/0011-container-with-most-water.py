class Solution:
    '''
    Time Complexity: O(n) because each element in the list is processed at most once.
    Space Complexity: O(1) as no extra space is used beyond a few variables.
    TWO POINTER APPROACH QUESTION
    '''
    def maxArea(self, height: List[int]) -> int:
        start=0
        end=len(height)-1
        maximumArea=0
        while start<end:
            width=end-start
            # Find the height by taking the minimum of the two heights at the pointers
            currentHeight=min(height[start],height[end])
            area=width*currentHeight  # area=width*height
            maximumArea=max(area,maximumArea)  # Update the maximum area if the current area is larger
            if height[start]<height[end]:
                start+=1
            else:
                end-=1
        
        return maximumArea
            