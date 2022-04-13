public class ReverseKGroup {

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
        // int reverseNum = 1;
        // ListNode tail;
        // ListNode curr = head;
        ListNode orgHead = head;

        head = reverseList(head, k, totReverse);

        return head;
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


        ListNode prev = head;
        ListNode curr = prev.next;
        if (curr == null)
            return head;
        ListNode next = curr.next;
        int currK = 0;

        while (currK < k && curr != null) {
            next = curr.next;
            currK++;
            curr.next = prev;
            prev = curr;
            curr = next;
        }


        if (reverseNum == k || next == null)
            return prev;
        ListNode ans = reverseList(next, k, reverseNum - k);
        head.next = ans;
        return prev;
    }
    
}
