import java.util.Arrays;
import java.util.HashMap;
import java.util.Stack;

public class NextGreaterElement {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        HashMap<Integer, Integer> nextGreatest = new HashMap<>();
        //the stack stores elements which are lower than the peek
        //i.e elements which their next greater haven't been found yet, are stored once their next greater is found, they will be added to the map, then popped from the stack
        //then the prev num will be pushed to the stack and the cycle continues
        Stack<Integer> prevNum = new Stack<>();

        for (int num: nums2){
            while (!prevNum.isEmpty() && num > prevNum.peek())
                nextGreatest.put(prevNum.pop(), num);
            
            prevNum.push(num);
        }

        for (int i = 0; i < nums1.length; i++)
            nums1[i] = nextGreatest.containsKey(nums1[i])?nextGreatest.get(nums1[i]):-1;


        return nums1;
    }



    public static void main(String[] args) {
        NextGreaterElement nx = new NextGreaterElement();
        int[] nums1 = {4,1,2}; 
        int[] nums2 = {1,3,4,2};
        System.out.println(Arrays.toString(nx.nextGreaterElement(nums1, nums2)));
    }
}
