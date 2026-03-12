class ListNode {
      int val;
      ListNode next;
      ListNode() {}
      ListNode(int val) { this.val = val; }
      ListNode(int val, ListNode next) { this.val = val; this.next = next; }
  }
public class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if(head == null || head.next == null)
            return head;
        ListNode tail = head;
        int len = 1;
        while(tail.next != null){
            len +=1;
            tail = tail.next;
        }
        k = k % len;
        if(k == 0)
            return head;
        ListNode newTali = head;
        for (int i = 0; i < len - k - 1; i++) {
            newTali = newTali.next;
        }
        ListNode newHead = newTali.next;
        newTali.next = null;
        tail.next = head;        
        return newHead;
        
    }
}