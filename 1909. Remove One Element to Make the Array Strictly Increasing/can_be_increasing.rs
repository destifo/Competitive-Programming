impl Solution {
    
    // O(n) time,
    // O(1) space,
    // Approach: array, 
    pub fn can_be_increasing(nums: Vec<i32>) -> bool {
        let mut nums = nums;
        let mut removed = 0;
        
        for i in 1..nums.len() {
            
            if nums[i-1] >= nums[i]{
                removed += 1;
                
                if i > 1 && nums[i-2] >= nums[i] {
                    nums[i] = nums[i-1];
                }
            }
        }
        
        return removed < 2;
        
    }
}