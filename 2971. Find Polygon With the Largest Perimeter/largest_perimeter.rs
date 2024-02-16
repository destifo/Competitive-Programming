impl Solution {
    
    // O(nlogn) time,
    // O(1) space,
    // Approach: greedy, sorting, prefix sum
    pub fn largest_perimeter(mut nums: Vec<i32>) -> i64 {
        nums.sort();
        let mut ans = -1 as i64;
        let mut agg = (nums[0] + nums[1]) as i64;
        
        for i in 2..nums.len() {
            let num = nums[i] as i64;
            if num < agg {
                ans = agg + num;
            }
            agg += num;
        }
        
        ans
    }
}