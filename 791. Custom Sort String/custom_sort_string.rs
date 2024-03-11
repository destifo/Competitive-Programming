use std::collections::HashMap;


impl Solution {
    
    // O(n) time,
    // O(n) space,
    // Approach: hashmap, counting
    pub fn custom_sort_string(order: String, s: String) -> String {
        let mut count = HashMap::new();
        for ch in s.chars() {
            *count.entry(ch).or_insert(0) += 1;
        }
        
        let mut ans: String = Default::default();
        for ch in order.chars() {
            if let Some(ch_count) = count.get(&ch) {
                ans.push_str(&ch.to_string().repeat(*ch_count as usize));
                count.remove(&ch);
            }
        }
        
        for (ch, ch_count) in count {
            ans.push_str(&ch.to_string().repeat(ch_count));
        }
        
        ans
    }
}