import java.util.Stack;

public class PalindromeLinkedList {
    public class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next;
        }
    }

    public boolean isPalindrome(ListNode head) {
        if (head.next == null)
            return true;
        
        Stack<Integer> stack = new Stack<>();

        ListNode curr = head;
        while (curr != null){
            stack.push(curr.val);
            curr = curr.next;
        }

        curr = head;
        while (!stack.isEmpty()){
            if (stack.pop() != curr.val)
                return false;
            curr = curr.next;
        }

        return true;
    }

    // using two pointers...O(n) time, O(1) space
    public boolean isPalindrome2(ListNode head) {
        if (head.next == null)
            return true;

        ListNode fast = head;
        ListNode slow = head;

        // get the middle of the list, fast -> end | null, slow -> middle
        while (fast != null && fast.next != null){
            fast = fast.next.next;
            slow = slow.next;
        }

        // reverse from the middle(slow) to the end(fast)
        ListNode prev = null;
        while (slow != null){
            ListNode temp = slow.next;
            slow.next = prev;
            prev = slow;
            slow = temp;
        }

        ListNode left = head;
        ListNode right = prev;

        while (right != null){
            if (left.val != right.val)
                return false;
            
            left = left.next;
            right = right.next;
        }


        return true;
    }
}
