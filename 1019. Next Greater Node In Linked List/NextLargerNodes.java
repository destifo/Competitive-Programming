import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

public class NextLargerNodes {
    
    public class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next;
        }
    }

    // did this one with big help, not gonna lie
    public int[] nextLargerNodes(ListNode head) {

        Stack<Integer> stack = new Stack<>();
        ArrayList<Integer> vals = new ArrayList<>();

        ListNode curr = head;
        while (curr != null){
            vals.add(curr.val);
            curr = curr.next;
        }

        int[] answer = new int[vals.size()];

        for (int i = 0; i < vals.size(); i++){
            while (!stack.isEmpty() && vals.get(stack.peek()) < vals.get(i)){
                answer[stack.pop()] = vals.get(i);
            }
            stack.push(i);
        }
        
        return answer;
        
    }

    
    public int[] nextLargerNodesInTheList(ListNode head) {
     
        
        ArrayDeque<Integer> queue = new ArrayDeque<>();
        ListNode reversed = reverseList(head);
        queue.add(reversed.val);
        ListNode curr = reversed.next;
        int size = 1;
        while (curr != null){
            if (queue.peekLast() < curr.val){
                queue.add(curr.val);
            }
            else{
                queue.add(queue.peekLast());
            }
            curr = curr.next;
            size++;
        }

        int[] answer = new int[size];
        curr = reversed;
        for (int i = size - 1; i >= 0; i--){
            if (queue.peek() == curr.val)
                answer[i] = 0;
            else
                answer[i] = queue.peek();

            queue.poll();
            curr = curr.next;
        }

        return answer;
    }

    private ListNode reverseList(ListNode head){
        ListNode prev = head;
        ListNode curr = prev.next;
        ListNode next = null;
        if (curr != null)
            next = curr.next;

        while (curr != null){
            curr.next = prev;
            prev = curr;
            curr = next;
            if (curr != null)
                next = curr.next;
        }
        head.next = null;
        head = prev;

        return prev;
    }
}
