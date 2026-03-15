class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        result = [0] * n
        stack = [] # monotnic decreasing storing indices
        for i in range(n):
            while stack and temperatures[stack[-1]]  < temperatures[i]:
                idx = stack.pop()
                result[idx] = i - idx 
            stack.append(i)
        return result
        

        