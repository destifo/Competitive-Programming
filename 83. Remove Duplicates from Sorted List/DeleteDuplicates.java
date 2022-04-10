public class DeleteDuplicates {
    public class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next;
        }
    }

    public ListNode deleteDuplicates(ListNode head) {
        if (head == null)
            return null;

        ListNode curr = head;
        ListNode next = head.next;

        while (next != null){
            if (curr.val == next.val){
                curr.next = next.next;
                next.next = null;
                next = curr.next;
            }else{
                curr = next;
                next = curr.next;
            }
        }

        return head;
    }
}
