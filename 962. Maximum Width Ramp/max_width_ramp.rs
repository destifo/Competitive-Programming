use std::cmp;


impl Solution {
    
    fn find_furthest_min(target: i32, nums: &Vec<i32>, stack: &Vec<usize>) -> usize {
        let mut lo = 0 as usize;
        let mut hi = stack.len()-1;
        let mut ans = 0 as usize;
        
        while lo <= hi && hi < stack.len() {
            let mid = lo + (hi-lo)/2;
            if nums[stack[mid]] <= target {
                ans = stack[mid];
                hi = mid-1;
            } else {
                lo = mid+1;
            }
        }
        return ans
    }
    
    
    // O(nlogn) time,
    // O(n) space,
    // Approach: monotonic stack, binary search, 
    pub fn max_width_ramp(nums: Vec<i32>) -> i32 {
        let mut dec_stack = Vec::new();
        let mut max_width = 0;
        
        for i in 0..nums.len() {
            let stack_len = dec_stack.len();
            if stack_len == 0 || nums[dec_stack[stack_len-1]] > nums[i] {
                dec_stack.push(i);
            } else {
                let furthest_min_index = Solution::find_furthest_min(nums[i], &nums, &dec_stack);
                max_width = cmp::max(max_width, i-furthest_min_index);
            }
        }
        return max_width as i32;
    }
}