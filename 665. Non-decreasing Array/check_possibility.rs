impl Solution {
    
    // O(n) time,
    // O(n) space,
    // Approach: array, suffix value
    pub fn check_possibility(nums: Vec<i32>) -> bool {
        
        let mut right_sorted = vec![false;nums.len()+1];
        right_sorted[nums.len()-1] = true;
        right_sorted[nums.len()] = true;
		
		// build suffix array to check if nums is sorted staring from the index onwards
        for i in (0..nums.len()-1).rev() {
            
			// when u get a next value lower than our current we break
            if nums[i] > nums[i+1]{
                break;
            }
            
            right_sorted[i] = true;
        }
        
        for i in 0..nums.len() {
            let sorted_middle = if (i == 0 as usize || i == nums.len() - 1 || (nums[i+1]-nums[i-1]) >= 0) {true} else { false };
            
			// check if we can modify the middle and also if the right is sorted starting from (i+1), 
            if sorted_middle && right_sorted[i+1] {
                return true;
            }
            
			// if the nums becomes unsorted, we break from our loop, that basically means we can't sort nums by modifying any value, 
			// as going forward we won't have a sorted left side of our nums array
            if i != 0 && nums[i] < nums[i-1] {
                break;
            }
        }
        
        return false;
    }
}