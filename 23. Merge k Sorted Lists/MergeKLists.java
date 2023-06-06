/**
 * https://leetcode.com/problems/merge-k-sorted-lists/
 */

public class MergeKLists {
    public class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next;
        }
    }

    public ListNode mergeKLists(ListNode[] lists) {
        int n = lists.length;
        if (n == 0)
            return null;
        int l = 0;
        int r = n - 1;

        while (l < r){
            if (l == r - 1){
                if (lists[l] != null)
                    lists[r] = merge(lists[l], lists[r]);
                return lists[r];
            }
            if (lists[l] != null)
                lists[l + 1] = merge(lists[l], lists[l + 1]);
            if (lists[r] != null)
                lists[r - 1] = merge(lists[r - 1], lists[r]);

            l = l + 1;
            r = r - 1;

        }
        return lists[(n / 2)];
    }

    public ListNode merge(ListNode list1, ListNode list2) {
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
