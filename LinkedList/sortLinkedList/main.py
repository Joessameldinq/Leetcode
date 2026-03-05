class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def merge(list1, list2):
            dummy = ListNode(0)
            cur = dummy
            while list1 and list2:
                if list1.val < list2.val:
                    cur.next = list1
                    list1 = list1.next
                else:
                    cur.next = list2
                    list2 = list2.next
                cur = cur.next
            if list1: cur.next = list1  
            if list2: cur.next = list2
            return dummy.next

        if not (head and head.next):
            return head

        # Find mid
        slow, fast = head, head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None  # Split the list

        left = self.sortList(head)
        right = self.sortList(slow)
        return merge(left, right)