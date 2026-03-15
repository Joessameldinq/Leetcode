class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        n = len(prices)
        nextSmallest = [0] * n
        stack = [] # monotonic increasing storing indices
        for i in range(n):
            while stack and prices[stack[-1]] >= prices[i]:
                idx = stack.pop()
                nextSmallest[idx] = prices[i]
            stack.append(i)
        for i in range(n):
            prices[i]= prices[i] - nextSmallest[i]
        return prices

        