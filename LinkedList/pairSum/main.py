# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head) -> int:

        slow , fast = head ,head # get middle using tortoise-hare algorithm
        max_value = 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        

        # revers the second half
        cur , prev = slow , None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        left , right = head , prev
        while right:
            max_value = max(max_value,left.val + right.val)
            left = left.next
            right = right.next
        return max_value
