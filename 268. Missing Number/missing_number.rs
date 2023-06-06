impl Solution {
    
    // O(n) time,
    // O(1) space,
    // Approach: bit manipulation, 
    pub fn missing_number(nums: Vec<i32>) -> i32 {
     
        let mut ans: i32 = nums.len() as i32;
        
        for i in 0..nums.len() {
            ans ^= (i as i32 ^ nums[i] as i32);            
        }
                
        return ans;
        
    }
}