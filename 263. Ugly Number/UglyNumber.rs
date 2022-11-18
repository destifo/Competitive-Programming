impl Solution {
    
    pub fn reduce_by_factor(mut num: i32, factor: i32) -> i32 {
        
        while num != 0 && (num % factor) == 0{
            num /= factor;
        }
        
        return num;
        
    }
    
    
    // O(logn) time,
    // O(1) space,
    // Approach: math, 
    pub fn is_ugly(n: i32) -> bool {
        
        let factors = [2, 3, 5];
        
        let mut num = n;
        for factor in factors {
            num = Solution::reduce_by_factor(num, factor);
        }
        
        return num == 1;
        
    }
}