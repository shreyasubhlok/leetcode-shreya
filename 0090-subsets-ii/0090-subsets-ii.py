class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=set()
        subset=[]
        
        def backtrack(i):
            if i>=len(nums):
                print(res)
                res.add(tuple(subset))
                return
                
            subset.append(nums[i])
            backtrack(i+1)
            
            subset.pop()
            backtrack(i+1)
        
        backtrack(0)
        return list(res)