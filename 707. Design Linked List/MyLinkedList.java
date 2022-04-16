/**
 * https://leetcode.com/problems/design-linked-list/submissions/
 */

public class MyLinkedList {

    private class Node {
        public int val;
        public Node next;

        public Node(int val) {
            this.val = val;
        }
    }

    Node head;
    private int size;

    public MyLinkedList() {
        this.size = 0;
        this.head = new Node(-1);
    }

    public int get(int index) {
        if (index < 0 || index >= this.size)
            return -1;

        int count = 0;
        Node curr = head;

        while (count < index){
            curr = curr.next;
            count++;
        }

        return curr.val;
    }

    public void addAtHead(int val) {
        this.addAtIndex(0, val);
    }

    public void addAtTail(int val) {
        this.addAtIndex(size, val);
            
    }

    public void addAtIndex(int index, int val) {
        if (index < 0 || index > size)
            return;

        int count = 0;
        Node curr = head;
        while (count < index){
            curr = curr.next;
            count++;
        }
        
        Node node = new Node(val);
        node.next = curr.next;
        curr.next = node;
        this.size++;

    }

    public void deleteAtIndex(int index) {
        if (index < 0 || index >= this.size)
            return;

        Node curr = head;
        int count = 0;
        while (count < index){
            curr = curr.next;
            count++;
        }

        curr.next = curr.next.next;
        this.size--;
    }


    public static void main(String[] args) {
        MyLinkedList myLinkedList = new MyLinkedList();
        myLinkedList.addAtHead(4);
        myLinkedList.get(1); // return 2
        myLinkedList.addAtHead(1);
        myLinkedList.addAtHead(5);
        myLinkedList.deleteAtIndex(3); // now the linked list is 1->3
        myLinkedList.addAtHead(7);
        myLinkedList.get(3); // return 2
        myLinkedList.get(3); // return 2
        myLinkedList.get(3); // return 2
        myLinkedList.addAtHead(1);
        myLinkedList.deleteAtIndex(4); // now the linked list is 1->3
    }
}
