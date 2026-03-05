# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNodes(self, head):
        if  not (head and head.next):
            return head
        def reverse(node):
            cur , prev = node , None
            while cur:
                cur.next , cur ,prev = prev , cur.next , cur
            return prev
        head = reverse(head)
        max_val = head.val
        cur = head
        while cur.next:
            if cur.next.val >= max_val:
                max_val = cur.next.val
                cur = cur.next
            else:
                cur.next = cur.next.next
        return reverse(head)


        