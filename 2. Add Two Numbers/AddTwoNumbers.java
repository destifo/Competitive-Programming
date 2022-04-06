public class AddTwoNumbers {
    // sweated on it with no help, damn felt good when it got accepted.
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
    public static ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int l1Len = 1;
        ListNode current = l1.next;
        while (current != null) {
            l1Len++;
            current = current.next;
        }
        
        int l2Len = 1;
        current = l2.next;
        while (current != null) {
            l2Len++;
            current = current.next;
        }
        int maxLen = Math.max(l2Len, l1Len);
        int minLen = Math.min(l1Len, l2Len);

        int addCount = 0;
        int leftOver = 0;
        ListNode result = new ListNode();

        ListNode l1Current = l1;
        ListNode l2Current = l2;
        ListNode resCurrent = result;
        for (int i = 0; i < minLen; i++){
            int tot;
            if (leftOver != 0){
                tot = l1Current.val + l2Current.val + 1;
                ListNode totNode = new ListNode(tot%10);
                resCurrent.next = totNode;
            }
            else {
                tot = l1Current.val + l2Current.val;
                ListNode totNode = new ListNode(tot%10);
                resCurrent.next = totNode;
            }
            if (tot > 9)
                leftOver = 1;
            else
                leftOver = 0;
            
            l1Current = l1Current.next;
            l2Current = l2Current.next;
            resCurrent = resCurrent.next;
            addCount++;
        }

        if (leftOver == 1 && addCount == maxLen) {
            ListNode left = new ListNode(1);
            resCurrent.next = left;
        }


        if (addCount != maxLen) {
            for (int i = minLen; i < maxLen; i++) {
                if (leftOver != 0){
                    ListNode left = new ListNode(1);
                    resCurrent.next = left;
                    resCurrent = resCurrent.next;
                }
                else{
                    ListNode left = new ListNode(0);
                    resCurrent.next = left;
                    resCurrent = resCurrent.next;
                }
                if (l1Len > l2Len) {
                    resCurrent.val += l1Current.val;
                    l1Current = l1Current.next;
                }else{
                    resCurrent.val += l2Current.val;
                    l2Current = l2Current.next;
                }
                if (resCurrent.val >= 10){
                    leftOver = 1;
                    resCurrent.val = resCurrent.val % 10;
                }
                else{
                    leftOver = 0;
                }
            }
        }

        if (leftOver != 0){
            ListNode left = new ListNode(1);
            resCurrent.next = left;
        }
        result = result.next;

        return result;
    }
    
    public static void main(String[] args) {
        ListNode list1 = new ListNode(1);
        list1.next = new ListNode(8);

        ListNode list2 = new ListNode(0);

        ListNode ans = addTwoNumbers(list1, list2);

        while (ans != null){
            System.out.println(ans.val);
            ans= ans.next;
        }


    }
}