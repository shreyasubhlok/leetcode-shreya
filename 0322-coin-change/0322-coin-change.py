class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins or amount<0:
            return -1
        if amount==0:
            return 0
        
        dp=[math.inf]*(amount+1)
        dp[0]=0
        
        for x in range(1,amount+1):
            for coin in coins:
                if x-coin>=0:
                    dp[x]=min(dp[x],dp[x-coin]+1)
        
        if dp[amount]!=math.inf:
            return dp[amount]
        else:
            return -1