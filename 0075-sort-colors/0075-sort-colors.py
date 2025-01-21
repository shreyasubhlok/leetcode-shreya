class Solution:
    #Time is O(n) and space(O(1))
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                # Swap the current element with the element at low
                nums[mid], nums[low] = nums[low], nums[mid]
                low += 1  # Move low forward
                mid += 1  # Move mid forward
            elif nums[mid] == 1:
                mid += 1 # Just move mid forward
            else:
                # Swap the current element with the element at high
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1  # Move high backward
        