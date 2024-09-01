class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x:int,y:int)->int:
            return x**2 + y**2
        
        max_heap=[]
        for point in points:
            x=point[0]
            y=point[1]
            d=-distance(x,y)
            
            heapq.heappush(max_heap,(d,point))
            
            if len(max_heap)>k:
                heapq.heappop(max_heap)
        
        return [point for (d,point) in max_heap]