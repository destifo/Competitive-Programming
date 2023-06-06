/**
 * https://leetcode.com/problems/sort-list/submissions/
 */

public class SortList {
    public class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next;
        }
    }

    // did it myself but I don't think it's an efficent algo
    public ListNode sortList(ListNode head) {
        if (head == null)
                return null;
        
        return mergeSort(head);
    }

    private ListNode mergeSort(ListNode head){
        if (head.next == null)
            return head;

        ListNode fast = head;
        ListNode slow = head;
        ListNode prev = head;

        while (fast != null && fast.next != null){
            fast = fast.next.next;
            prev = slow;
            slow = slow.next;
        }

        prev.next = null;
        head = mergeSort(head);
        slow = mergeSort(slow);

        return merge(head, slow);
    }

    // [4, 5, 4, 3]
    // [4, 5] U [3, 4]
    // 
    private ListNode merge(ListNode left, ListNode right){
        ListNode head;
        if (left.val > right.val)
            head = right;
        else
            head = left;

        ListNode currLeft = left;
        ListNode currRight = right;

        while (currLeft != null && currRight != null){
            if (currLeft.val < currRight.val && (currLeft.next == null || currLeft.next.val >= currRight.val)){
                ListNode temp = currLeft.next;
                currLeft.next = currRight;
                currLeft = currRight;
                currRight = temp;
            }else if (currLeft.val > currRight.val && (currRight.next == null || currRight.next.val >= currLeft.val)){
                ListNode temp = currRight.next;
                currRight.next = currLeft;
                currRight = temp;
            }else if (currLeft.val == currRight.val){
                ListNode temp = currLeft.next;
                currLeft.next = currRight;
                currLeft = currRight;
                currRight = temp;
            }
            else if (currLeft.val < currRight.val){
                currLeft = currLeft.next;
            }else{
                currRight = currRight.next;
            }
        }

        return head;

    }
}
