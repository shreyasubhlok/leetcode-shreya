class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Approach 1 (preferred apprach) to use set - better approach
        # time is o(n) and space is o(n)...on time is better then o nlogn which will be there in case of                 sorting
        mySet=set()
        for num in nums:
            if num in mySet:
                return True
            else:
                mySet.add(num)
        
        return False
    
    # Apprach 2
    def containsDuplicateUsingSorting(self, nums: List[int]) -> bool:
        #Approach 2 : sorting
        #Sorting is not optimal: Sorting the list takes O(n log n) time, which is less efficient than using a          set which takes O(n) time.
        # Time complexity is O(n log n) due to sorting
        # Space complexity is O(1) if we don't count the input array
        nums.sort()
        for i in range(len(nums) - 1):  # Iterate until the second last element
            if nums[i] == nums[i + 1]:
                return True
        return False