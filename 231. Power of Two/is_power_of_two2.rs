impl Solution {
    
    // O(1) time,
    // O(1) space,
    // Approach: bit manipulation, 
    pub fn is_power_of_two(n: i32) -> bool {
        let n = n as i64;
        n != 0 && (n & n-1) == 0
    }
}