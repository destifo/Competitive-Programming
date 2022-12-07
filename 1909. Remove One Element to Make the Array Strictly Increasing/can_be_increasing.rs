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

    // O(n) time,
    // O(n) space,
    // Approach: array, 
    pub fn can_be_increasing2(nums: Vec<i32>) -> bool {
        
        let mut left_sorted = vec![false;nums.len()];
        let mut right_sorted = vec![false;nums.len()];
        
        left_sorted[0] = true;
        for i in 1..nums.len() {
            
            if nums[i-1] >= nums[i] {
                break;
            }
            
            left_sorted[i] = true;  
        }
        
        right_sorted[nums.len()-1] = true;
        for i in (0..nums.len()-1).rev() {
            
            if nums[i] >= nums[i+1] {
                break;
            }
            
            right_sorted[i] = true;
        }
        
        let mut answer = false;
        
        for i in 0..nums.len() {
            
            if answer == true {
                break;
            }
            
            let is_right_sorted = if (i == nums.len()-1) {true} else {right_sorted[i+1]};
            let is_left_sorted = if (i == 0) {true} else {left_sorted[i-1]};
            
            // println!("{} {} {}", i, is_left_sorted, is_right_sorted);
            
            let mut is_sorted = (is_left_sorted) && (is_right_sorted);
            if i == 0 || i == nums.len()-1 {
                answer = is_sorted;
                continue;
            }
            
            let middle_sorted = nums[i-1] < nums[i+1];
            is_sorted = is_sorted && middle_sorted;
            
            answer = is_sorted;
        }
        
        return answer;
    }
}