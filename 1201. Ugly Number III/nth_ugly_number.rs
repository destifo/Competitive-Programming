impl Solution {
    
    pub fn gcd(a: i64, b: i64) -> i64 {
        
        let mut x = a;
        let mut y = b;
        
        while y != 0 {
            let temp = x;
            x = y;
            y = (temp%y);
        }
        
        return x;
    }
    
    pub fn lcm(a: i64, b: i64) -> i64 {
        
        return (a*b) / Solution::gcd(a, b);
        
    }
    
    pub fn ugly_numbers_count(n: i64, a: i64, b: i64, c: i64) -> i64 {
        
        let a_mult = n / a;
        let b_mult = n / b;
        let c_mult = n / c;
        
        let a_c = n / Solution::lcm(a, c);
        let a_b = n / Solution::lcm(a, b);
        let c_b = n / Solution::lcm(c, b);
        
        let a_b_c = n / Solution::lcm(a, Solution::lcm(b, c));
        
        return a_mult + b_mult + c_mult - a_b - a_c - c_b + a_b_c;
        
    }
    
    
    pub fn is_divisible(num: i64, a: i64, b: i64, c: i64) -> bool {
        
        if num % a == 0 || num % b == 0 || num % c == 0 {
            return true;
        }
        
        return false;
        
    }
    
    
    // O(logn) time,
    // O(logn) space,
    // Approach: binary search, math
    pub fn nth_ugly_number(n: i32, a: i32, b: i32, c: i32) -> i32 {
        
        let mut lo = 1 as i64;
        let mut hi = i32::MAX as i64;
        
        while lo <= hi {
            
            let mid = lo + (hi-lo)/2;
            let count = Solution::ugly_numbers_count(mid, a as i64, b as i64, c as i64);

            if count == n as i64 && Solution::is_divisible(mid, a as i64, b as i64, c as i64) {
                return mid as i32;
            }
            else if count >= n  as i64 {
                hi = mid-1;
            }
            else {
                lo = mid + 1;
            }
            
        }
        
        return -1;
    }
}