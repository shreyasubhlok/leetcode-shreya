class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums)<target:
            return 0
        windowsum = nums[0]
        i = 0
        j = 0
        minlen = math.inf
        while j < len(nums):
            print(j)
            print(i)
            if windowsum < target:
                if j!=len(nums)-1:
                    j+=1
                    windowsum = windowsum + nums[j]
                else:
                    break
            else:
                currlen = j - i + 1
                minlen = min(currlen, minlen)
                windowsum = windowsum - nums[i]
                i = i + 1
        return minlen