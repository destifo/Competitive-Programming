import java.util.HashSet;

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
        ListNode dummy = new ListNode(0, head);
        ListNode curr = head;
        ListNode prev = dummy;
        HashSet<Integer> duplicates = new HashSet<>();
        while (curr != null && curr.next != null){
            if (curr.val == curr.next.val){
                duplicates.add(curr.val);
            }

            Boolean wasInwhile = false;
            while (duplicates.contains(curr.val)){
                ListNode temp = curr;
                prev.next = curr.next;
                curr = curr.next;
                temp.next = null;
                wasInwhile = true;
            }

            if (!wasInwhile){
                prev = curr;
                curr = curr.next;
            }
        }

        return dummy.next;
    }
}
