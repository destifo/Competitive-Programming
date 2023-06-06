import java.util.ArrayDeque;
import java.util.Deque;

class ShortestSubarray {
    public int shortestSubarray(int[] nums, int k) {
        Deque<long[]> sumAtIndex = new ArrayDeque<>();
        long min_len = Long.MAX_VALUE;
        long tot = 0;

        for (int i = 0; i < nums.length; i++){
            tot += nums[i];
            if (tot >= k){
                min_len = Math.min(i + 1, min_len);
            }

            while (!sumAtIndex.isEmpty() && tot <= sumAtIndex.peekLast()[0])
                sumAtIndex.removeLast();

            while (!sumAtIndex.isEmpty() && tot - sumAtIndex.peekFirst()[0] >= k){
                min_len = Math.min(min_len, i - sumAtIndex.removeFirst()[1]);
            }

            long[] pair = {tot, i};
            sumAtIndex.addLast(pair);
        }

        return min_len == Long.MAX_VALUE?-1:(int)(min_len);
    }

    public static void main(String[] args) {
        ShortestSubarray sub = new ShortestSubarray();
        int[] nums = {17,85,93,-45,-21};
        int k = 150;
        System.out.println(sub.shortestSubarray(nums, k));
    }
}