use std::cmp::min;

fn is_power_five(s: &str) -> bool {
    let mut num = i32::from_str_radix(s, 2).unwrap();
    while num % 5 == 0 && num > 1 {
        num /= 5;
    }
    
    num == 1
}


fn count_beautiful(l: usize, r: usize, s: &String) -> i32 {
    let mut min_partition = i32::MAX;
    
    if l == s.len() {
        return 0;
    }
    
    // partition
    if (r == s.len() || &s[r..r+1] != "0") && is_power_five(&s[l..r]) {
        let result = count_beautiful(r, r+1, s);
        if result != i32::MAX {
            min_partition = min(min_partition, 1 + result);
        }
    }
    
    if r < s.len() {
        min_partition = min(min_partition, count_beautiful(l, r+1, s));
    }
    
    min_partition
}


impl Solution {
    pub fn minimum_beautiful_substrings(s: String) -> i32 {
        if &s[..1] == "0" {
           return -1;
        }
        
        let answer = count_beautiful(0, 1, &s);
        if answer == i32::MAX {
            return -1;
        }
        answer
    }
}