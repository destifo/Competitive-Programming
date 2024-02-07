use std::collections::HashMap;


impl Solution {
    
    // O(n) time, n -> s.len()
    // O(1) space,
    // Approach: hashmap, sorting
    pub fn frequency_sort(s: String) -> String {
        let mut count: HashMap<char, i32> = HashMap::new();
        for ch in s.chars() {
            *count.entry(ch).or_insert(0) += 1;
        }
        
        let mut entries: Vec<(char, i32)> = count.iter().map(|(&k, &v)| (k, v)).collect();
        entries.sort_by_key(|&(_, v)| v);
        
        let mut ans = String::new();
        for &(k, curr_count) in entries.iter().rev() {
            ans.push_str(&k.to_string().repeat(curr_count as usize));
        }
        
        ans
    }
}