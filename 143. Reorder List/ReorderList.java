public class ReorderList {
    public class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next;
        }
    }

    public void reorderList(ListNode head) {
        if (head == null || head.next == null)
            return;
        ListNode fast = head;
        ListNode slow = head;

        while (fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
        }

        ListNode prev = null;
        while (slow != null){
            ListNode next = slow.next;
            slow.next = prev;
            prev = slow;
            slow = next;
        }

        ListNode currFront = head;
        ListNode currBack = prev;

        while (currFront != null && currBack != null){
            ListNode next1 = currFront.next;
            ListNode next2 = currBack.next;
            currFront.next = currBack;
            currBack.next = next1;
            currFront = next1;
            currBack = next2;
        }
        if (currBack != null)
            currBack.next = null;

        if (currFront != null)
            currFront.next = null;

    }
}
