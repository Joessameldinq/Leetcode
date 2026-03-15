import heapq
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        dummy = ListNode()
        tail = dummy
        pq = []
        for i , lst in enumerate(lists):
            if lst:
                heapq.heappush(pq,(lst.val,i,lst))
        while pq:
            _,i,minNode = heapq.heappop(pq)
            if minNode.next:
                heapq.heappush(pq,(minNode.next.val,i,minNode.next))
            tail.next = minNode
            tail = tail.next
        return dummy.next