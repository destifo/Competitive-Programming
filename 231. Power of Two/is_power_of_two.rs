impl Solution {
    
    // O(logn) time,
    // O(logn) space,
    // Approach: recursion, 
    pub fn is_power_of_two(n: i32) -> bool {
        if n == 1 {
            return true;
        }
        
        if n <= 0 {
            return false;
        }        
        
        match n % 2 {
            1 => false,
            _ => Solution::is_power_of_two(n/2),
        }
    }
}