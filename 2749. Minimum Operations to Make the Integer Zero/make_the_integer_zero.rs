fn is_power_of_two_sum(num: i64, k: i64) -> bool {
    num.count_ones() as i64 <= k && k <= num
}


fn is_valid_cost(cost: i32, num1: i32, num2: i32) -> bool {
    let diff = (num1 as i64 - (num2 as i64 * cost as i64));
    is_power_of_two_sum(diff, cost as i64)
}


impl Solution {

    // O(1) time,
    // O(1) space,
    // Approach: math, 
    pub fn make_the_integer_zero(num1: i32, num2: i32) -> i32 {
        
        for cost in 0..=60 {
            if is_valid_cost(cost as i32, num1, num2) {
                return cost as i32;
            }
        }

        -1
    }
}
