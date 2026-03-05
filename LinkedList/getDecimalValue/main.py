# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head) -> int:
        if not head:
            return 0
        val = 0
        cur = head
        while cur:
            val = 2 * val + cur.val
            cur = cur.next
        return val
        