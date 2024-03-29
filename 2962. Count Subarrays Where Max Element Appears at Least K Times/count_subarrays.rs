impl Solution {
    
    // O(n) time,
    // O(1) space,
    // Approach: sliding window, counting
    pub fn count_subarrays(nums: Vec<i32>, k: i32) -> i64 {
        let n = nums.len();
        let max_val = *nums.iter().max().unwrap();
        let mut max_count = 0;
        let mut ans = 0;
        
        let mut left = 0;
        for right in 0..n {
            if nums[right] == max_val {
                max_count += 1;
            }
            
            while max_count >= k {
                if nums[left] == max_val {
                    max_count -= 1;
                }
                left += 1;
            }
            
            ans += left as i64;
        }
        
        ans
    }
}