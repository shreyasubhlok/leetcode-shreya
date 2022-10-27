class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxAvg = -inf
        i = 0
        j = 0
        w = 0
        total = 0

        while j < len(nums):
            total += nums[j]
            w += 1

            if w == k:
                maxAvg = max(total, maxAvg)
                total -= nums[i]
                i += 1
                w -= 1

            j += 1


        return maxAvg/k
        