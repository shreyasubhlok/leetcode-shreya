class Solution:
    """
    Algo -
    1. Initialize a prefix sum array
    2. Calculate the prefix sum based on weight
    3. Generate a random number between 0 and total_weight
    4. use binary search to find the appropriate index
    """

    def __init__(self, w: List[int]):
        self.prefixSum = []
        currSum = 0
        for weight in w:
            currSum += weight
            self.prefixSum.append(currSum)
        self.totalSum = currSum

    def pickIndex(self) -> int:
        target = random.randint(1, self.totalSum)
        low = 0
        high = len(self.prefixSum) - 1
        while low < high:
            mid = (low + high) // 2
            if target > self.prefixSum[mid]:
                low = mid + 1
            else:
                high = mid
        return low


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
