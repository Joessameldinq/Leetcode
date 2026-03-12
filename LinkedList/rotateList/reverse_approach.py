class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        
        # Get length
        n, cur = 0, head
        while cur:
            n += 1
            cur = cur.next
        
        k = k % n
        if k == 0:
            return head

        # Reverse entire list
        # Reverse first (n-k) elements
        # Reverse last k elements
        
        def reverse(node, steps):
            prev = None
            cur = node
            for _ in range(steps):
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return prev, node, cur  # new_head, new_tail, remainder

        # Step 1: Reverse full list
        rev_head, _, _ = reverse(head, n)

        # Step 2: Reverse first k elements
        new_head, mid_tail, remainder = reverse(rev_head, k)

        # Step 3: Reverse remaining (n-k) elements
        mid_tail.next, _, _ = None, None, None
        last_head, _, _ = reverse(remainder, n - k)
        mid_tail.next = last_head

        return new_head