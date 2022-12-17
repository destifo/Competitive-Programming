impl Solution {
    
    
    // Euclid's gcd algorithm
    fn gcd(divd: i32, divisor: i32) -> i32 {
        
        if divisor == 0 {
            return divd;
        }
        
        return Solution::gcd(divisor, divd%divisor);
    }
    
    
    // O(logn) time, n --> max jug capacity
    // O(1) space,
    // Approach: math, 
    pub fn can_measure_water(jug1_capacity: i32, jug2_capacity: i32, target_capacity: i32) -> bool {
        
        let gcd = Solution::gcd(jug1_capacity, jug2_capacity);
        let tot_vol = jug1_capacity + jug2_capacity;
        
        return target_capacity % gcd == 0 && target_capacity <= tot_vol;
        
    }
}