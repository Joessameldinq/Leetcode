class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        map = {0:-1}
        runningsum = 0
        answer = 0

        for i , number in enumerate(nums):
            runningsum += 1 if number == 1 else -1
            if runningsum in map:
                answer = max(answer,i-map[runningsum])
            else:
                map[runningsum] = i
        return answer
        