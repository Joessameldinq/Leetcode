# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def splitListToParts(self, head, k: int):
        def get_size(node):
            cur = node
            length = 0
            while cur:
                length += 1
                cur = cur.next
            return length
        size = get_size(head)
        base_size = size // k
        extra_size = size % k
        parts = [None] * k

        node = head
        prev = None
        for i in range(k):
            parts[i] = node
            for j in range(base_size + (1 if extra_size > 0 else 0)):
                    prev = node
                    node = node.next
            if prev:
                 prev.next = None
            
            if extra_size > 0:
                 extra_size -=1
        return parts


        