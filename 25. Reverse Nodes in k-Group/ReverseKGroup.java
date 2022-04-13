public class ReverseKGroup {

    // did 90% of this without help. 
    public class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next;
        }
    }

    public ListNode reverseKGroup(ListNode head, int k) {
        if (head == null)
            return null;
        int totReverse = size(head);

        ListNode ans = reverseList(head, k, totReverse);

        return ans;
    }

    private int size(ListNode head){
        int count = 0;
        ListNode curr = head;
        while (curr != null){
            count++;
            curr = curr.next;
        }

        return count;
    }

    private ListNode reverseList(ListNode head, int k, int reverseNum) {
        
        if (reverseNum < k)
            return head;
        
        if (k == 1)
            return head;
        
        reverseNum -=k;


        ListNode prev = head;
        ListNode curr = prev.next;
        ListNode next = curr.next;
        int currK = 1;

        while (currK < k) {
            currK++;
            curr.next = prev;
            prev = curr;
            curr = next;
            if (curr != null)
                next = curr.next;
        }

        

        head.next = null;
        if (curr == null){
            return prev;
        }
        
        
        ListNode ans = reverseList(curr, k, reverseNum);
        head.next = ans;
        return prev;
    }
    
}
