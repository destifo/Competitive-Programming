use std::collections::HashMap;


impl Solution {
    
    // O(n) time, 2 passes
    // O(1) space,
    // Approach: hashmap, counting
    pub fn first_uniq_char(s: String) -> i32 {
        let mut count: HashMap<char, i32> = HashMap::new();
        let chars: Vec<char> = s.chars().collect();
        
        for ch in &chars {
            let mut prev_count = 0;
            if let Some(cnt) = count.get(&ch) {
                prev_count = *cnt;
            }
            count.insert(*ch, prev_count+1);
        }
        
        for i in 0..chars.len() {
            let curr = chars[i];
            if let Some(cnt) = count.get(&curr) {
                if *cnt == 1 {
                    return i as i32;
                }
            }
        }
        
        -1
    }
}