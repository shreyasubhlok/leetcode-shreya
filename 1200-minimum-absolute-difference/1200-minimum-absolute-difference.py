class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minDiff=math.inf
        res=[]
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i]<minDiff:
                minDiff=arr[i+1]-arr[i]
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i]==minDiff:
                res.append([arr[i],arr[i+1]])
        
        return res
             
            