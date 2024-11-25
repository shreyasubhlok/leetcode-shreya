class Solution:
    # time : ologn )coz of binary search
    # space: O(1)
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if len(nums) == 0:
            return [-1, -1]
        
        def findBound(isFirst):
            left = 0
            right = len(nums) - 1
            bound=-1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    bound = mid
                    if isFirst:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return bound

        firstPosition = findBound(True)
        lastPosition = findBound(False)

        return [firstPosition, lastPosition]