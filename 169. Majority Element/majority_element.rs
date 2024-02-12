impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> i32 {
        let mut ans = nums[0];
        let mut count = 0;
        
        for num in nums {
            if num == ans {
                count += 1;
            } else {
                count -= 1;
            }

            if count == 0 {
                ans = num;
                count = 1;
            }
        }
        
        ans
    }
}