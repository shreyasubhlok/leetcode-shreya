class Solution:
    #Time is O(n) and space O(1)
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates=[]
        i=0 # start an index at 0
        while i < len(nums):
            val = abs(nums[i]) # get the absolute value of the current element
            if nums[val-1] < 0: # check if we've already marked this index negative
                duplicates.append(val)
            else:
                nums[val-1] = -nums[val-1] # flip the sign of nums[val - 1] to mark it visited
            i += 1
        return duplicates

        '''
        class Solution:
    #Time is O(n) and space O(n)
    def findDuplicates(self, nums: List[int]) -> List[int]:
        visited = set()
        res = []
        for elem in nums:
            if elem in visited:
                res.append(elem)
            visited.add(elem)
        return res     
        '''