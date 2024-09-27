class Solution:
    """
    Time Complexity: O(logN), N = size of the given array.
    Reason: We are using binary search to search the target.
    Space Complexity: O(1)
    """

    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            # Case 1: find target
            if nums[mid] == target:
                return mid

            # Case 2: subarray on mid's left is sorted
            if nums[start] <= nums[mid]:
                if target >= nums[start] and target <= nums[mid]:
                    end = mid - 1  # element exist
                else:
                    start = mid + 1  # element doesn't exist

            # Case 3: subarray on mid's right is sorted.
            if nums[mid] <= nums[end]:
                if target >= nums[mid] and target <= nums[end]:
                    start = mid + 1  # element exist
                else:
                    end = mid - 1  # element doesn't exist
        return -1
