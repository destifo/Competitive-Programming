impl Solution {

    // O(n) time,
    // O(n) space,
    // Approach: simulation, 
    pub fn largest_good_integer(num: String) -> String {
        let mut ans = String::from("");
        let mut max_num = -1;
        let digits: Vec<char> = num.chars().collect();

        let mut index = 0 as usize;
        while index < digits.len()-2 {
            if digits[index] == digits[index+1] && digits[index] == digits[index+2] {
                let substring: String = digits[index..index+3].iter().collect();
                let num: i32 = substring.parse().unwrap();

                if num > max_num {
                    max_num = num;
                    ans = substring;
                }
                index += 2;
            }
            index += 1;
        }

        ans
    }   
}