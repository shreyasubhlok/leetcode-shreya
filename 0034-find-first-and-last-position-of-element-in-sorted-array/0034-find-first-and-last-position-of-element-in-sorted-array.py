class Solution:
    # time : ologn )coz of binary search
    # space: O(1)
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if len(nums) == 0:
            return [-1, -1]

        def findBound(isFirst):
            """
            Helper function to find the first or last occurrence of the target.
            :param isFirst: bool - True to find the first occurrence, False for the last
            :return: int - Index of the bound
            """
            left = 0
            right = len(nums) - 1
            bound = -1
            while left <= right:
                mid = (left + right) // 2  # Calculate the mid-point

                if nums[mid] == target:
                    bound = mid  # Update the bound
                    if isFirst:
                        right = mid - 1  # Search the left half for the first occurrence
                    else:
                        left = mid + 1  # Search the right half for the last occurrence
                elif nums[mid] < target:
                    left = mid + 1  # Move right
                else:
                    right = mid - 1  # Move left
            return bound

        # Find the first and last occurrences of the target
        firstPosition = findBound(True)
        lastPosition = findBound(False)

        return [firstPosition, lastPosition]