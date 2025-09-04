impl Solution {

    // O(1) time,
    // O(1) space,
    // Approach: math, 
    pub fn find_closest(x: i32, y: i32, z: i32) -> i32 {
        let (diff1, diff2) = ((z-x).abs(), (z-y).abs());
        if diff1 == diff2 {
            0
        } else if diff1 < diff2 {
            1
        } else {
            2
        }
    }
}
