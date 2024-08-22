class Solution:
    # Dynamic Programming bottom up apprach
    # Time is o(n) and space is o(n) - efficient solution
    def climbStairs(self, n: int) -> int:
        # if there's is only 1 step, there's only one way to climb it
        if n == 1:
            return 1

        # initialize an array name dp with zeros to perform bottom up apprach and fill data from bottom to up
        # dp[i] will hold the number of ways to reach the ith step
        dp = [0] * (n + 1)
        dp[1] = 1  # Base Case: 1 way to climb 1 step
        dp[2] = 2  # Base Case: 2 ways to climb 2 steps (1 step+1 step, or 2 steps at once_

        # use dynamic programming to fill DP array from bottom to up
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]  # The value at dp[n] is the number of ways to reach the nth step