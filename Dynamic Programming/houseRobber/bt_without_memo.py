class Solution:
    def rob(self, nums: list[int]) -> int:

        def recur(currentIndex)->int:
            if currentIndex >= len(nums):
                return 0
            return max(nums[currentIndex] + recur(currentIndex+2),recur(currentIndex+1))
        return recur(0)
        