impl Solution {
    
    fn find_good_job(target: i32, arr: &Vec<Vec<i32>>) -> usize {
        let mut answer = 0;
        let mut lo = 0;
        let mut hi = arr.len()-1;
        
        while lo <= hi {
            let mid = ((lo+hi)/2);
            let difficulty = arr[mid][0];
            
            if target >= difficulty {
                answer = mid;
                lo = mid + 1;
            } else {
                hi = mid-1;
            }
        }
        
        return answer;
    }
    
    
    // O(mlogn + n) time, n --> len(profit) m --> len(worker),
    // O(n) space,
    // Approach: binary search, sorting, 
    pub fn max_profit_assignment(difficulty: Vec<i32>, profit: Vec<i32>, worker: Vec<i32>) -> i32 {
        let mut d_to_p = vec![vec![0; 2];difficulty.len()];
        for i in 0..difficulty.len() {
            d_to_p[i][0] = difficulty[i];
            d_to_p[i][1] = profit[i];
        }
        
        d_to_p.sort();
        let mut prev_max = 0;
        for i in 0..profit.len() {
            let curr_profit = d_to_p[i][1];
            if prev_max > curr_profit {
                d_to_p[i][1] = prev_max;
            } else {
                prev_max = curr_profit;
            }
        }
        
        let mut max_profit = 0;
        for capability in worker {
            if capability >= d_to_p[0][0] {
                let good_job_index = Solution::find_good_job(capability, &d_to_p);
                max_profit += d_to_p[good_job_index][1];
            }
        }
        
        return max_profit;
    }
}