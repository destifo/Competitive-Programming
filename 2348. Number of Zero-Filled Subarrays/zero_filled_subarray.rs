impl Solution {

    // O(n) time,
    // O(1) space,
    // Approach: two pointers, math
    pub fn zero_filled_subarray(nums: Vec<i32>) -> i64 {
        let mut ans = 0;
        
        let mut i = 0 as usize;
        while i < nums.len() {
            if nums[i] != 0 {
                i += 1;
                continue;
            }

            let mut j = i + 1;
            while j < nums.len() {
                if nums[j] != 0 {
                    break;
                }
                j += 1
            }
            let length = (j-i) as i64;
            let subarrays = (length*(length+1))/2;
            ans += subarrays;
            i = j;
        }

        ans
    }
}
