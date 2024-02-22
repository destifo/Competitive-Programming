impl Solution {
    
    // O(log(right)) time,
    // O(1) space,
    // Approach: bit manipulation, 
    pub fn range_bitwise_and(mut left: i32, mut right: i32) -> i32 {
        let mut shifted = 0;
        
        while left != right {
            left >>= 1;
            right >>= 1;
            shifted += 1;
        }
        
        left <<= shifted;
        return left;
    }
}