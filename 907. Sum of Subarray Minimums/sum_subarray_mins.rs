
impl Solution {
    // O(n) time,
    // O(n) space,
    // Approach: monotonic stack, 
    pub fn sum_subarray_mins(arr: Vec<i32>) -> i32 {
       
        let MOD = i64::pow(10, 9) + 7;
        let mut mins_index: Vec<usize> = Vec::new();
        let mut sum = 0 as i64;
        
        for index in 0..arr.len() {
            let num = arr[index];
            
            while mins_index.len() > 0 && num < arr[*mins_index.last().unwrap()] {
                
                let curr_index = mins_index.pop().unwrap();
                let curr_min = arr[curr_index];
                let left = if mins_index.len() > 0 { *mins_index.last().unwrap() as i32} else { -1 };
                let right = index;
                
                let right_sum = ((right-curr_index) as i32);
                let left_sum = (curr_index as i32 - left);
                sum += ((left_sum * right_sum) as i64 * curr_min as i64) % MOD;
                // sum %= MOD;
            }
            
            mins_index.push(index);
        }
        
        // println!("{:?}", mins_index);
        let right = arr.len();
        while mins_index.len() > 0 {
                
                let curr_index = mins_index.pop().unwrap();
                let curr_min = arr[curr_index];
                let left = if mins_index.len() > 0 { *mins_index.last().unwrap() as i32} else { -1 };
                
                let right_sum = ((right-curr_index) as i32);
                let left_sum = (curr_index as i32 -left);
            
                sum += ((left_sum * right_sum) as i64 * curr_min as i64) % MOD;
                // sum %= MOD;
        }
        
        return (sum % MOD) as i32;
    }
}