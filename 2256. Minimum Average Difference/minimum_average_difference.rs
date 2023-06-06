impl Solution {
    
    // O(n) time,
    // O(n) space,
    // Approach: prefix sum, 
    pub fn minimum_average_difference(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut prefix_sum = vec![0 as i64;n+1];
        
        let mut tot = 0 as i64;
        for (i, num) in (&nums).iter().enumerate() {
            tot += (*num as i64);
            prefix_sum[i+1] = tot;
        }
        
        
        let mut answer = n;
        let mut min_diff = i32::MAX as i64;
        
        for i in 0..n {
            
            let left_avg = prefix_sum[i+1] / (i+1) as i64;
            let right_avg = if (i != n-1) { (prefix_sum[n] - prefix_sum[i+1]) / (n-i-1) as i64 } else { 0 as i64};
            
            let diff = (right_avg-left_avg).abs();
            
            if diff < min_diff {
                answer = i;
                min_diff = diff;
            }  
        }
        
        return answer as i32;
        
    }
}