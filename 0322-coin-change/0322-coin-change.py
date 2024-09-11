
class Solution:
    # DP problem bottom up apporach...
    # Time complexity: O(m * n), where m is the number of coins and n is the target amount
    # space complexity: o(n),  n is the target amount
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Edge case- if no coins are provided or amount is negative or zero
        if not coins or amount < 0:
            return -1
        if amount == 0:
            return 0

        # Initialize a dp array where dp[i] represents the minimum number of coins needed to make i amount
        # Start with math.inf (infinity), meaning the amount is not yet reachable
        dp = [math.inf] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins are needed to make amount 0

        for x in range(1, amount + 1):  # Loop through each amount from 1 to the target amount,x represents the current amount we are trying to form
            for coin in coins:  # Try each coin from the list of coins to see if it can be used to make the current amount `x`.
                if x - coin >= 0:  # Only proceed if the current coin can be used to make `x`. If it is negative, this coin cannot be used to form `x`
                    dp[x] = min(dp[x], dp[x - coin] + 1)  # This means: check if using the current coin gives a better (lower) number of coins than the previously recorded result in dp[x].

        # If dp[amount] is still infinity, that means it's impossible to form the amount with the given coins
        if dp[amount] != math.inf:
            return dp[amount]  # Return the minimum number of coins needed to form the amount
        else:
            return -1  # Return -1 if it's not possible to form the amount



"""
The DP tree shows how each value in the DP array depends on previous values
dp[5] (using coin 5) = dp[5 - 5] + 1 = dp[0] + 1 = 1
 └─ dp[0] = 0

dp[5] (using coin 2) = dp[5 - 2] + 1 = dp[3] + 1 = 3
 └─ dp[3] (using coin 2) = dp[3 - 2] + 1 = dp[1] + 1 = 2
     └─ dp[1] = 1

dp[5] (using coin 1) = dp[5 - 1] + 1 = dp[4] + 1 = 5
 └─ dp[4] (using coin 2) = dp[4 - 2] + 1 = dp[2] + 1 = 2
     └─ dp[2] (using coin 2) = dp[2 - 2] + 1 = dp[0] + 1 = 1

"""
