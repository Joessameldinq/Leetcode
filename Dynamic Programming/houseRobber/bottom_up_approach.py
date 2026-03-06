class Solution:
    def rob(self, nums: list[int]) -> int:
        prev , current = 0 , 0
        for num in nums:
            prev , current = current , max(current,prev+num)
        return current
        