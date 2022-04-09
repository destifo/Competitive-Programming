/**
 * https://leetcode.com/problems/reverse-linked-list/
 */

public class ReverseList {
    public class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next;
        }
    }

    public ListNode reverseList(ListNode head) {
        ListNode next;
        ListNode prev = head;
        ListNode curr = head.next;
        ListNode orgHead = head;

        while (curr != null)
        {
            next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        orgHead = null;
        head = prev;

        return head;
    }
}
