# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head):
        temp = ListNode(0,head)
        prev , current = temp , head
        while current and current.next:
            # save pointers
            next_pair = current.next.next
            next = current.next

            # reverse
            next.next = current
            current.next = next_pair
            prev.next = next

            # update
            prev = current
            current = next_pair
        return temp.next
        