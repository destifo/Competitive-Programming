import java.util.Arrays;

class MyCircularDeque {

    private int[] queue;
    private int front;
    private int rear;
    private int size = 0;

    public MyCircularDeque(int k) {
        this.queue = new int[k];
        this.front = k - 1;
        this.rear = 0;
    }



    public boolean insertFront(int value) {
        if (isFull()) return false;

        queue[front] = value;
        front = (front - 1 + queue.length) % queue.length;
        size++;
        return true;
    }
    
    public boolean insertLast(int value) {
        if (isFull()) return false;

        queue[rear] = value;
        rear = (rear + 1) % queue.length;
        size++;
        return true;
    }
    
    public boolean deleteFront() {
        if (isEmpty()) return false;

        front = (front + 1) % queue.length;
        size--;
        return true;
    }
    
    public boolean deleteLast() {
        if (isEmpty()) return false;

        rear = (rear - 1 + queue.length) % queue.length;
        size--;
        return true;
    }
    
    public int getFront() {
        if (isEmpty()) return -1;
        return queue[(front + 1) % queue.length];
    }
    
    public int getRear() {
        if (isEmpty()) return -1;

        return queue[(rear - 1 + queue.length) % queue.length];
    }
    
    public boolean isEmpty() {
        return this.size == 0;
    }
    
    public boolean isFull() {
        return this.size == queue.length;  
    }


    @Override
    public String toString(){
        return Arrays.toString(queue);
    }

    public static void main(String[] args){
        MyCircularDeque myCircularDeque = new MyCircularDeque(2);
        
        System.out.println(myCircularDeque.insertFront(7));
        System.out.println(myCircularDeque.deleteLast());
        System.out.println(myCircularDeque.getFront());
        System.out.println(myCircularDeque.insertLast(5));
        System.out.println(myCircularDeque.insertFront(0));
        System.out.println(myCircularDeque.getFront());
        System.out.println(myCircularDeque.getRear());
        //System.out.println(myCircularDeque.isEmpty());
        //System.out.println(myCircularDeque.deleteFront());

        //System.out.println(myCircularDeque.isFull());
        //System.out.println(myCircularDeque.deleteLast());

        System.out.println(myCircularDeque.toString());
    }
        
}

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * MyCircularDeque obj = new MyCircularDeque(k);
 * boolean param_1 = obj.insertFront(value);
 * boolean param_2 = obj.insertLast(value);
 * boolean param_3 = obj.deleteFront();
 * boolean param_4 = obj.deleteLast();
 * int param_5 = obj.getFront();
 * int param_6 = obj.getRear();
 * boolean param_7 = obj.isEmpty();
 * boolean param_8 = obj.isFull();
 */