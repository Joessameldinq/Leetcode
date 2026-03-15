class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nextGreater = {}
        stack = [] # monotonic decreasing
        for val in nums2:
            while stack and stack[-1] < val:
                nextGreater[stack.pop()] = val
            stack.append(val)
        while stack:
            nextGreater[stack.pop()] = -1
        return [nextGreater[x] for x in nums1]
        