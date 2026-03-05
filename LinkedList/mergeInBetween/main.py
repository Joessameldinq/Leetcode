# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:

        begin_node = list1
        end_node = list1
        cur = list2
        for i in range(1,a):
            begin_node = begin_node.next
        for i in range(b):
            end_node = end_node.next
        begin_node.next = list2
        while cur.next:
            cur = cur.next
        cur.next = end_node.next
        return list1

        