impl Solution {

    // O(logn) time,
    // O(logn) space,
    // Approach: recursion
    pub fn is_power_of_three(n: i32) -> bool {
        if n == 1 {
            return true;
        }
        
        if n <= 0 || n % 3 != 0 {
            return false;
        }
        
        Solution::is_power_of_three(n/3)
    }

    // O(logn) time,
    // O(1) space,
    // Approach: recursion
    pub fn is_power_of_three2(mut n: i32) -> bool {
        
        while n > 1 {
            if n % 3 != 0 {
                return false;
            }

            n /= 3;
        }

        n == 1
    }
}