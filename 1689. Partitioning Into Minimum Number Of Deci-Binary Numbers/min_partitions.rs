impl Solution {

    // O(n) time, n -> number of digits,
    // O(n) space, n -> number of digits,
    // Approach: The minimum number of deci-binary numbers needed is equal to the maximum digit in the given number, string, 
    pub fn min_partitions(n: String) -> i32 {

        // this one is really slow, 25-30ms runtime
        // let digits: Vec<i32> = n.chars().map(|d| d.to_string().parse::<i32>().unwrap()).collect();

        // this one is faster, like 2ms runtime
        let digits: Vec<i32> = n.chars().map(|d| d.to_digit(10).unwrap() as i32).collect();
        
        digits.into_iter().max().unwrap()
    }
}