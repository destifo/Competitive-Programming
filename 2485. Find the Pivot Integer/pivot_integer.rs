impl Solution {
    
    // O(n) time, one pass
    // O(1) space,
    // Approach: prefix sum, math
    pub fn pivot_integer(n: i32) -> i32 {
        let summation = (n*(n+1))/2;
        
        let mut curr_tot = 0;
        for i in 1..=n {
            let right = summation-curr_tot;
            curr_tot += i;
            let left = curr_tot;
            if left == right {
                return i;
            }
        }
        
        -1
    }
}