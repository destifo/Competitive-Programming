use std::collections::HashMap;

fn convert_num_to_digit_count(n: i32) -> HashMap<char, i32> {
    let num_str = n.to_string();
    let mut digit_count = HashMap::new();

    for ch in num_str.chars() {
        *digit_count.entry(ch).or_insert(0) += 1;
    }

    digit_count
}

fn compare_digit_counts(count1: &HashMap<char, i32>, count2: &HashMap<char, i32>) -> bool {
    for (key, val) in count1 {
        match count2.get(key) {
            Some(val2) => {
                if val != val2 {
                    return false;
                }
            },
            None => return false
        }
    }
    
    true
}


impl Solution {
    pub fn reordered_power_of2(n: i32) -> bool {
        let num_str = n.to_string();
        let digit_count = convert_num_to_digit_count(n);

        let base_num = 10_i32.pow((num_str.len() - 1) as u32);
        let base_power = (base_num as f64).log2().ceil() as u32;

        let end_num = 10_i32.pow((num_str.len()) as u32);
        let end_power = (end_num as f64).log2().floor() as u32;

        for i in base_power..=end_power {
            let possible_num = 2_i32.pow(i) as i32;
            let count = convert_num_to_digit_count(possible_num);

            if compare_digit_counts(&digit_count, &count) {
                println!("{}", possible_num);
                return true;
            }
        }

        false
    }
}