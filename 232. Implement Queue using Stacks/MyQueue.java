import java.util.EmptyStackException;
import java.util.Stack;

public class MyQueue {
    private Stack<Integer> stack = new Stack<>();
    
    public MyQueue() {
        
    }
    
    public void push(int x) {
        this.stack.push(x);
    }
    
    public int pop() {
        if (this.empty())
            throw new EmptyStackException();
        Stack<Integer> temp = new Stack<>();
        int value;
        int stackSize = this.stack.size();
        for (int i = 0; i < stackSize - 1; i++){
            value = stack.pop();
            temp.push(value);
        }
        int poped = this.stack.pop();
        int tempStackSize = temp.size();
        for (int i = 0; i < tempStackSize; i++)
            this.stack.push(temp.pop());
        
        return poped;
        
    }
    
    public int peek() {
        if (this.empty())
            throw new EmptyStackException();
        Stack<Integer> temp = new Stack<>();
        int value;
        int stackSize = this.stack.size();
        for (int i = 0; i < stackSize - 1; i++){
            value = stack.pop();
            temp.push(value);
        }
        int poped = this.stack.pop();
        int tempStackSize = temp.size();
        this.stack.push(poped);
        for (int i = 0; i < tempStackSize; i++)
            this.stack.push(temp.pop());
        
        return poped;
        
    }
    
    public boolean empty() {
        boolean result = this.stack.isEmpty();
        return result;
    }

    public static void main(String[] args) {
        MyQueue myQueue = new MyQueue();
        myQueue.push(1);
        myQueue.push(2);
        myQueue.push(3);
        myQueue.push(5);
        System.out.println(myQueue.peek());
        System.out.println(myQueue.pop());
        System.out.println(myQueue.pop());
        
    }

}


