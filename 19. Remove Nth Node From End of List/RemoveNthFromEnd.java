public class RemoveNthFromEnd {

    public class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next;
        }
    }

    public ListNode removeNthFromEnd(ListNode head, int n) {
        int sz = 0;
        ListNode curr = head;
        while (curr != null){
            curr = curr.next;
            sz++;
        }
        
        if (sz < 2)
            return null;
        
        if (sz == n){
            head = head.next;
            return head;
        }

        curr = head;
        for (int i = 1; i < sz - n; i++)
            curr = curr.next;
        
        ListNode nextToCurr = curr.next;
        curr.next = nextToCurr.next;
        nextToCurr.next = null;

        return head;
    }  
}
