impl Solution {
    
    // O(n^2) time,
    // O(n) space, 
    // Approach: dp, bottom up, 
    pub fn can_jump(nums: Vec<i32>) -> bool {
        let mut dp: Vec<i32> = vec![0; nums.len()];
        dp[nums.len()-1] = 1;
        
        for i in (0..nums.len()-1).rev() {
            let jumps: usize = nums[i] as usize;
            let mut found = false;
            for jump in 1..jumps+1 {
                if i+jump < nums.len() && dp[i+jump] == 1 {
                    found = true;
                    break;
                }
            }
            if found {
                dp[i] = 1;
            }
            
        }
        return dp[0] == 1;
    }

    
    // O(n) time,
    // O(1) space, 
    // Approach: greedy, 
    pub fn can_jump(nums: Vec<i32>) -> bool {
        let mut farthest: i32 = 0;
        
        for i in 0..nums.len() {
            let jump: i32 = nums[i];
            if i as i32 <= farthest {
                farthest = cmp::max(farthest, i as i32+jump);
            } else {
                return false
            }
        }
        
        return true;
    }
}