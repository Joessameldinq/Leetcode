# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head):
        if not head:
            return head
        def gcd(a,b):
            if b== 0:
                return a
            return gcd(b,a%b)
        current = head
        while current.next:
            val = gcd(current.val , current.next.val)
            temp = current.next
            newnode = ListNode(val,temp)
            current.next = newnode
            current = temp
        return head

        
        