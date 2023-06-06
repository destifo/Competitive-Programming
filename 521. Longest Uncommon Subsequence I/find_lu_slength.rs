use std::cmp;


impl Solution {
    
    // O(n) time, takes linear time for comparing strings
    // O(1) space,
    // Approach: string, brain teaser
    pub fn find_lu_slength(a: String, b: String) -> i32 {
        return if a != b {cmp::max(a.len(), b.len()) as i32} else {-1};
    }
}