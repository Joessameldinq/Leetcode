class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        """
        let dp[i] -> fewest number of coins needed to reach ammount i
        dp[i] = for all coins min(1 + dp[i-coin])
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(amount+1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i] , 1 + dp[i-coin])
        return dp[amount] if dp[amount] != float('inf') else -1