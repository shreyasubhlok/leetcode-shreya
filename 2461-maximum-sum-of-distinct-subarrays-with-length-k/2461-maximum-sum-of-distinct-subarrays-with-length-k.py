from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) < k:
            return 0
        maxsum = 0
        windowsum = 0
        hm = {}
        for i in range(k):
            if nums[i] not in hm:
                hm[nums[i]] = 1
            else:
                hm[nums[i]] = hm[nums[i]] + 1
            windowsum += nums[i]
            if len(hm) == k:
                maxsum = windowsum
                break

        j = k
        i = j - k
        while j < len(nums):
            #remove from map nums[i]
            hm[nums[i]] -= 1
            if hm[nums[i]] == 0:
                del hm[nums[i]]
            curr = nums[j]

            #add num[j] to map
            if nums[j] not in hm:
                hm[nums[j]] = 1
            else:
                hm[nums[j]] = hm[nums[j]] + 1
            windowsum = windowsum + nums[j]-nums[i]
            if len(hm) == k:
                maxsum = max(windowsum, maxsum)
            j = j + 1
            i = i + 1

        return maxsum




if __name__=="__main__":
    nums = [1, 5, 4, 2, 9, 9, 9]
    k = 3
    sol=Solution()
    res=sol.maximumSubarraySum(nums,k)
    print("2461. Maximum Sum of Distinct Subarrays With Length K: ",res)