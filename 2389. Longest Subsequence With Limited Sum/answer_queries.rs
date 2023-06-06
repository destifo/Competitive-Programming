impl Solution {
    
    fn find_longest_subsequence(target: i32, pf_sum: &Vec<i32>) -> i32 {
        let mut answer = 0;
        let mut lo = 0;
        let mut hi = (pf_sum.len()-1) as i32;
        
        while lo <= hi {
            let mid = ((lo+hi)/2) as usize;
            let num = pf_sum[mid];
            
            if num == target {
                return (mid+1) as i32;
            } else if num < target {
                answer = (mid+1) as i32;
                lo = answer;
            } else {
                hi = (mid-1) as i32;
            } 
        }
        
        return answer;
    }
    
    
    // O(n + mlogn) time,
    // O(n + m) space,
    // Approach: prefix sum, binary search, 
    pub fn answer_queries(nums: Vec<i32>, queries: Vec<i32>) -> Vec<i32> {
        let mut nums = nums;
        nums.sort();
        let mut prefix_sum = vec![0;nums.len()];
        let mut tot = 0;
        
        for i in 0..nums.len() {
            tot += nums[i];
            prefix_sum[i] = tot;
        }
        
        let mut answer = vec![0; queries.len()];
        for (i, query) in queries.iter().enumerate() {
            answer[i] = Solution::find_longest_subsequence(*query, &prefix_sum);
        }
        
        return answer;
    }
}