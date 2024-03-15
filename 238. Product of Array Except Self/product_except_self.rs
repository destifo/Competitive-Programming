impl Solution {
    
    // O(n) time,
    // O(n) space,
    // Approach: prefix sum(prod), 
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let (mut prefix, mut suffix) = (vec![1;n+1], vec![1;n+1]);
        
        for i in 0..n {
            prefix[i+1] = prefix[i] * nums[i];
        }
        
        for i in (0..n).rev() {
            suffix[i] = suffix[i+1] * nums[i];
        }
        
        let mut ans = vec![1;n];
        for i in 0..n {
            ans[i] = prefix[i] * suffix[i+1];
        }
        
        ans
    }
}