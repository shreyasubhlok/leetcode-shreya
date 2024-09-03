class Solution:
    # time is o(n2) due to the nested loops after sorting
    # space is o(1) excluding the space required to store the output
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        res = []
        nums.sort()  # Sort the array to apply the two-pointer technique
        for i in range(len(nums) - 2):
            start = i + 1
            end = len(nums) - 1

            # Skip duplicate elements for the first position in the triplet
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # continue meaning skips the current iteration of the loop and moves to the next iteration.

            while start < end:
                sum = nums[i] + nums[start] + nums[end]
                if sum < 0:  # If the sum is less than zero, we need a larger value, so increment start
                    start = start + 1
                elif sum > 0:  # If the sum is greater than zero, we need a smaller value, so decrement end
                    end = end - 1
                else:
                    temp = [nums[i], nums[start], nums[end]]
                    res.append(temp)
                    start = start + 1
                    end = end - 1
                    # Skip over any duplicate elements after finding a valid triplet
                    while start < end and nums[start] == nums[start - 1]:
                        start = start + 1
                    while start < end and nums[end] == nums[end + 1]:
                        end = end - 1

        return res
