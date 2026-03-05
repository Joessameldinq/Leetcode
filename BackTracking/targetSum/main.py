class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        n = len(nums)

        def backtrack(idx,current):
            if idx == n:
                return 1 if current == target else 0
            add = backtrack(idx+1,current+nums[idx])
            subtract = backtrack(idx+1,current-nums[idx])
            
            return add + subtract
        return backtrack(0,0)
            
            
