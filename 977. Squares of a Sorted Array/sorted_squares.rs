impl Solution {
    
    // O(n) time,
    // O(n) space,
    // Approach: two pointers, 
    pub fn sorted_squares(nums: Vec<i32>) -> Vec<i32> {        
        let (mut left, mut right) = (0, 0);
        for (i, num) in nums.iter().enumerate() {
            if *num >= 0 {
                break;
            }
            right = i+1;
        }
        left = right-1;
        
        let mut answer = vec![];
        while (left >= 0 && left < nums.len()) && right < nums.len() {
            let left_sqr = nums[left]*nums[left];
            let right_sqr = nums[right]*nums[right];
            if left_sqr < right_sqr {
                answer.push(left_sqr);
                left -= 1;
            } else {
                answer.push(right_sqr);
                right += 1;
            }
        }
        
        while left >= 0 && left < nums.len() {
            answer.push(nums[left]*nums[left]);
            left -= 1;
        }
        
        while right < nums.len() {
            answer.push(nums[right]*nums[right]);
            right += 1;
        }
        
        answer
    }
}