# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeNodes(self, head):
        if head is None:
            return head
        
        dummy = ListNode()
        current = dummy
        temp = head 
        sum = 0
        while temp:
            if temp.val == 0:
                temp = temp.next
                while temp and temp.val != 0:
                    sum += temp.val
                    temp = temp.next
                if sum > 0:  
                    current.next = ListNode(sum)
                    current = current.next 
                sum = 0
        return dummy.next
            
