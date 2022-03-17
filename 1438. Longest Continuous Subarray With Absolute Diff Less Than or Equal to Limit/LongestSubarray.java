import java.util.ArrayDeque;
import java.util.Deque;
import java.util.LinkedList;
import java.util.Queue;

public class LongestSubarray {
    public int longestSubarray(int[] nums, int limit) {
        int n = nums.length;
        int longest = Integer.MIN_VALUE;
        Deque<Integer> minQ = new LinkedList<>();
        Deque<Integer> maxQ = new LinkedList<>();
        
        int left = 0;

        for (int right = 0; right < n; right++){
            while (!maxQ.isEmpty() && nums[right] > maxQ.peekLast())
                maxQ.pop();
            maxQ.addLast(nums[right]);
        
            while (!minQ.isEmpty() && nums[right] < minQ.peekLast())
                minQ.pop();
            minQ.addLast(nums[right]);


            if (maxQ.peek() - minQ.peek() <= limit){
                longest = Math.max(longest, right - left + 1);
                right++;
            }
            else {
                if (maxQ.peek() == nums[left])
                    maxQ.removeFirst();
                if (minQ.peek() == nums[left])
                    minQ.removeFirst();
                
                left++;
            }
        }

        return longest; 
    }

    public static void main(String[] args) {
        LongestSubarray ls = new LongestSubarray();
        int[] nums = {2,2,2,4,4,2,5,5,5,5,5,2};
        int limit = 2;
        System.out.println(ls.longestSubarray(nums, limit));
    }
}
