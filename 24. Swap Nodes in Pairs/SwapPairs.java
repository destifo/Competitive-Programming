/**
 * https://leetcode.com/problems/swap-nodes-in-pairs/submissions/
 */

public class SwapPairs {
    
    public class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next;
        }
    }

    // first try, under 10 mins, it worked. ezy for medium questions
    public ListNode swapPairs(ListNode head) {
        if (head == null)
            return null;
        
        ListNode curr = head;
        ListNode next = curr.next;
        
        if (next == null)
            return curr;
        
        ListNode temp = next.next;
        next.next = curr;
        curr.next = null;

        if (temp == null)
            return next;
            
        curr.next = swapPairs(temp);
        return next;
        
    }
}
