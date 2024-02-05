use std::collections::HashMap;
use std::cmp::min;


impl Solution {
    
    // O(n) time, one pass
    // O(1) space,
    // Approach: hashmap, counting
    pub fn first_uniq_char(s: String) -> i32 {
        let mut count: HashMap<char, i32> = HashMap::new();
        let chars: Vec<char> = s.chars().collect();
        let mut min_index: HashMap<char, i32> = HashMap::new();
        
        for i in 0..chars.len() {
            let ch = chars[i];
            let mut prev_count = 0;
            if let Some(cnt) = count.get(&ch) {
                prev_count = *cnt;
            } else {
                min_index.insert(ch, i as i32);
            }
            count.insert(ch, prev_count+1);
        }
        
        let mut ans = s.len() as i32;
        for (ch, cnt) in count {
            if cnt == 1 {
                ans = min(ans, *min_index.get(&ch).unwrap());
            }
        }
        
        if ans == s.len() as i32 {
            return -1;
        }
        
        ans
    }
}