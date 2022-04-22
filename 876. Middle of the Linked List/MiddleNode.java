/**
 * https://leetcode.com/problems/middle-of-the-linked-list/submissions/
 */


public class MiddleNode {
    // 100% faster leetcode says...well it was nothing to get hyped...probably everyone has provided the same solution...may be, but it says 0ms another scenario is the time is too small for whn the algorithm tried to round it and it ended up being zero
    public static class ListNode {
        int val;
        ListNode next;
        ListNode () {}
        ListNode (int val) {
            this.val = val;
        }
        ListNode(int val, ListNode next) {
            this.val = val;
            this.next = next;
        }
    }
    public static ListNode middleNode(ListNode head) {
        int listLength = 0;
        ListNode curr = head;
        while (curr != null) {
            curr = curr.next;
            listLength++;
        }

        int mid = listLength/2 + 1;
        ListNode result = head;
        for (int i = 0; i < mid; i++)
            result = result.next;
            
        return result;
    }

    // using two pointers
    public static ListNode middleNode2(ListNode head){
        ListNode slow = head;
        ListNode fast = head;

        while (fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
        }

        return slow;
    }
    
}