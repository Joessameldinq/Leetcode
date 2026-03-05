class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        """
        let P = sum of +ve
            N = sum of -ve
            P - N = target
            P + N = total
            P = (target + total ) / 2
        the problem turns to find number of subsets that sum to P
        """
        total = sum(nums)

        if abs(target) > total or (target + total) % 2 != 0:
            return 0
        
        sub_sum = (total + target) // 2
        # dp[i] = number of ways to reach sum i
        dp = [0] * (sub_sum+1)
        dp[0] = 1
        for num in nums:
            for j in range(sub_sum,-1,-1):
                if j - num < 0:
                    continue
                dp[j] += dp[j-num]
        return dp[sub_sum]