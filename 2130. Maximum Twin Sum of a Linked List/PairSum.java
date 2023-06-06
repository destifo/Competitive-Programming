public class PairSum {

    public class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next;
        }
    }

    public int pairSum(ListNode head) {
        ListNode fast = head;
        ListNode slow = head;

        // find the middle of the linkedlist
        while (fast != null && fast.next != null){
            fast = fast.next.next;
            slow = slow.next;
        }

        // reverse from end to the middle of the linkedlist
        ListNode prev = null;
        while (slow != null){
            ListNode temp = slow.next;
            slow.next = prev;
            prev = slow;
            slow = temp;
        }

        // now calculate the pairsum of each twin nodes
        int maxPairSum = Integer.MIN_VALUE;
        while (prev != null){
            maxPairSum = Math.max(maxPairSum, head.val + prev.val);
            head = head.next;
            prev = prev.next;
        }

        return maxPairSum;
    }
    
}
