class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        """
        dp[i] -> length of LIS ending at i
        """
        max_lis = 1
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i] , 1 + dp[j])
            if dp[i] > max_lis:
                max_lis = dp[i]
        return max_lis