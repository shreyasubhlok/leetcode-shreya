class Solution:
    # time: olog(n)
    # space: o(1)
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        # If the list has one element or is already sorted, return the first element
        if len(nums) == 1 or nums[0] < nums[len(nums) - 1]:
            return nums[0]

        start = 0
        end = len(nums) - 1

        while start < end:
            mid = (start + end) // 2
            # If the middle element is less than the last element,
            # it means the smallest value is in the left portion (including mid)
            if nums[mid] < nums[end]:
                end = mid
            else:
                start = mid + 1

        # When the loop ends, start will be at the minimum element
        return nums[start]
