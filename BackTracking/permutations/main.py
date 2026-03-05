class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        sol = []
        def backtrack(begin):
            if begin >= len(nums):
                sol.append(nums[:])
                return

            for i in range(begin,len(nums)):
                nums[begin] , nums[i] = nums[i] , nums[begin]
                backtrack(begin+1)
                nums[begin] , nums[i] = nums[i] , nums[begin]

        backtrack(0)
        return sol
                    