/**
 * https://leetcode.com/problems/merge-two-sorted-lists/
 */

public class MergeTwoLists {
    public class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next;
        }
    }

    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if (list1 == null)
            return list2;

        if (list2 == null)
            return list1;


        if (list1.val <= list2.val){
            ListNode curr = list1;
            ListNode temp = list2;
            ListNode next = curr.next;
            while (curr != null && temp != null){
                if (next == null || temp.val < next.val){
                    curr.next = temp;
                    curr = curr.next;
                    temp = next;
                    next = curr.next;
                }
                else{
                    curr = next;
                    next = curr.next;
                }

            }
            
            return list1;
        }
        else{
            ListNode curr = list2;
            ListNode temp = list1;
            ListNode next = curr.next;
            while (curr != null && temp != null){
                if (next == null || temp.val < next.val){
                    curr.next = temp;
                    curr = curr.next;
                    temp = next;
                    next = curr.next;
                }
                else{
                    curr = next;
                    next = curr.next;
                }

            }

            return list2;
        }
           
        
    }
}
