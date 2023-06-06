impl Solution {
    
    // O(logn) time,
    // O(1) space,
    // Approach: binary search, math
    pub fn is_perfect_square(num: i32) -> bool {
        let mut low = 1;
        let mut hi = (46341); // 46,341 is the maximum root u can have for a i32 type
        
        while low <= hi {
            let mid = low + (hi-low)/2;
            let square = (mid*mid);
            
            if square == num {
                return true;
            }
            else if square < num{
                low = mid+1;
            }
            else {
                hi = mid-1;
            }
        }
        
        return false;
    }
}