class Solution:
    def rob(self, nums: list[int]) -> int:
        dp = [-1] * len(nums)
        def recur(currentIndex)->int:
            if currentIndex >= len(nums):
                return 0
            if dp[currentIndex] != -1:
                return dp[currentIndex]
            dp[currentIndex] = max(nums[currentIndex] + recur(currentIndex+2),recur(currentIndex+1))
            return dp[currentIndex]
        return recur(0)
        