impl Solution {
    
    // O(n^2) time,
    // O(n^2) space,
    // Approach: bottom up dp, sorting
    pub fn largest_divisible_subset(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut dp: Vec<Vec<i32>> = vec![vec![];n];
        let mut answer: Vec<i32> = vec![];
        let mut nums = nums;
        nums.sort();
        
        for i in (0..n).rev() {
            let mut longest = vec![];
            for j in i..n {
                if nums[j] % nums[i] == 0 {
                    if longest.len() < dp[j].len() {
                        longest = dp[j].clone();
                    }
                }
            }
            dp[i].push(nums[i]);
            dp[i].extend(longest);
            if answer.len() < dp[i].len() {
                answer = dp[i].clone();
            }
        }
        
        answer
    }
}