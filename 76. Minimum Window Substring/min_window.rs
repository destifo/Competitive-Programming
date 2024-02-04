use std::collections::HashMap;


fn are_equal(needle: &HashMap<char, i32>, haystack: &HashMap<char, i32>) -> bool {
    for (k, v) in needle {
        if let Some(count) = haystack.get(k) {
            if *count < *v {
                return false;
            }
        } else {
            return false;
        }
    }
    
    return true;
}


impl Solution {
    
    
    // O(n + m) time, n -> s.len(), m -> t.len(),
    // O(1) space,
    // Approach: sliding window, hashmap
    pub fn min_window(s: String, t: String) -> String {
        let (mut left, mut right) = (0, 0);
        let mut answer = "";
        
        let mut t_dict: HashMap<char, i32> = HashMap::new();
        for ch in t.chars() {
            let mut count = 1;
            if let Some(prev_count) = t_dict.get(&ch) {
                count += *prev_count 
            }
            t_dict.insert(ch, count);
        }
        let mut window: HashMap<char, i32> = HashMap::new();
        let chars: Vec<char> = s.chars().collect();
        
        while right < chars.len() {
            let curr = chars[right];
            let mut curr_count = 0;
            if let Some(count) = window.get(&curr) {
                curr_count = *count;
            }
            window.insert(curr, curr_count+1);
            
            while are_equal(&t_dict, &window) {
                
                // udpate our answer
                let slice = &s[left..right+1];
                if answer == "" || slice.len() < answer.len() {
                    answer = slice;
                }
                
                // udpate our window
                let left_char = chars[left];
                let left_count = window.get(&left_char).unwrap();
                window.insert(left_char, left_count-1);
                left += 1;
            }
            
            right += 1;
        }
        
        answer.to_string()
    }
}