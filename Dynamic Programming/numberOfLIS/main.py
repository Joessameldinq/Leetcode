class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        solutions = 0
        max_lis = 1
        n = len(nums)
        """
        dp[i] -> length of LIS ending at i
        """
        dp = [1] * n
        count = [1] * n # # of LIS ending at i
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if 1 + dp[j] > dp[i]:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif 1 + dp[j] == dp[i]:
                        count[i] += count[j]
            if dp[i] > max_lis:
                max_lis = dp[i]
                solutions = count[i]
            elif dp[i] == max_lis:
                solutions += count[i]
        return solutions

s = Solution()
nums = [2,2,2,2,2]
print(s.findNumberOfLIS(nums))
