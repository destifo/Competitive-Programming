use std::collections::{HashSet};


impl Solution {
    
    pub fn digits(num: i32) -> usize {
        let mut divider = 10;
        let mut digits = 1 as usize;
        
        while num / divider != 0 {
            divider *= 10;
            digits += 1;
        }
        
        return digits;
    }
    
    
    pub fn populate_digits(num: i32, evens: &mut Vec<i32>, odds: &mut Vec<i32>, odd_indices: &mut HashSet<usize>) {
         
        let mut index = 0 as usize;
        let mut num = num;
        while num > 0 {
            let digit = num % 10;
            if digit % 2 == 0 {
                evens.push(digit);
            }
            else {
                odds.push(digit);
                odd_indices.insert(index);
            }
            index += 1;
            num /= 10;
        }
    }
    
    
    // O(1) time, 9 digits at max
    // O(1) space,
    // Approach: math, array
    pub fn largest_integer(num: i32) -> i32 {
        let mut evens = Vec::new();
        let mut odds = Vec::new();
        let mut odd_indices: HashSet<usize> = HashSet::new();
        
        let digits = Solution::digits(num);
        
        Solution::populate_digits(num, &mut evens, &mut odds, &mut odd_indices);
        
        let mut answer = 0;
        let mut multiplier = 1;
        let mut curr_odd = 0;
        let mut curr_even = 0;
        
        for i in (0..digits) {
            if odd_indices.contains(&i) {
                answer += (odds[curr_odd]*multiplier);
                curr_odd += 1;
            }
            else {
                answer += (evens[curr_even]*multiplier);
                curr_even += 1;
            }
            multiplier *= 10;
        }
        
        return answer;
    }
}