use std::collections::HashMap;


impl Solution {
    
    // O(n) time,
    // O(1) space,
    // Approach: hashmap, sorting, 
    pub fn frequency_sort(s: String) -> String {
        
        let mut letter_count: HashMap<char, i32> = HashMap::new();
        
        for ch in s.chars() {
            let mut count = 0;
            
            if letter_count.contains_key(&ch) {
                count = *letter_count.get(&ch).unwrap_or(&0);
            }
            
            count += 1;
            letter_count.insert(ch, count); 
        }
        
        let mut char_count_pair = Vec::new();
        for (ch, count) in letter_count {
            char_count_pair.push((count, ch));
        }
        
        char_count_pair.sort();
        char_count_pair.reverse();
        let mut char_list = Vec::new();
        
        for char_info in char_count_pair {
            for _ in 0..char_info.0 {
                char_list.push(char_info.1);
            }
        }
        
        let answer = char_list.iter().collect::<String>();
        
        answer
        
    }
}