class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # The time complexity of the binary search algorithm is oLog(n)
        # space complexity is o(1)- we are using only we extra variables
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
