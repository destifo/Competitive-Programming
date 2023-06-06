impl Solution {
    
    pub fn shift_to_even(left: usize, right: usize, nums: &Vec<i32>) -> usize {
        let mut right = right;
        while left < right && nums[right] % 2 == 1 {
            right -= 1;
        }
        
        return right;
    }
    
    pub fn shift_to_odd(left: usize, right: usize, nums: &Vec<i32>) -> usize {
        let mut left = left;
        while left < right && nums[left] % 2 == 0 {
            left += 1;
        }  
        
        return left;
    }
    
    
    // O(n) time,
    // O(1) space,
    // Approach: two pointers, array, 
    pub fn sort_array_by_parity(nums: Vec<i32>) -> Vec<i32> {
        let mut left = 0 as usize;
        let mut right = nums.len()-1;
        left = Solution::shift_to_odd(left, right, &nums);
        right = Solution::shift_to_even(left, right, &nums);
        
        let mut nums = nums;
        while left < right {
            let temp = nums[left];
            nums[left] = nums[right];
            nums[right] = temp;
            
            left = left + 1;
            left = Solution::shift_to_odd(left, right, &nums);
            right = right - 1;
            right = Solution::shift_to_even(left, right, &nums);
        }
        
        return nums;
    }
}