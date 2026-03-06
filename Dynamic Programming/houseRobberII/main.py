class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        def helper(lst)->int:
            prev , current = 0 , 0
            for num in lst:
                prev , current = current , max(current,prev+num)
            return current
        return max(helper(nums[:n-1]) , helper(nums[1:n]))