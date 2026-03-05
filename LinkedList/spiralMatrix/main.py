# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head) :
        grid = [[-1] * n for _ in range(m)]
        top = 0
        bottom = m-1
        left = 0
        right = n - 1
        cur = head
        while cur and top <= bottom and left <= right:
            for i in range(left,right+1):
                if cur:
                    grid[top][i] = cur.val
                    cur = cur.next
                else:
                    break
            top += 1
            for i in range(top,bottom+1):
                if cur:
                    grid[i][right] = cur.val
                    cur = cur.next
                else:
                    break
            right -=1
            for i in range(right,left-1,-1):
                if cur:
                    grid[bottom][i] = cur.val
                    cur = cur.next
                else:
                    break
            bottom -=1
            for i in range(bottom,top-1,-1):
                if cur:
                    grid[i][left] = cur.val
                    cur = cur.next
                else:
                    break
            left +=1
        return grid





        