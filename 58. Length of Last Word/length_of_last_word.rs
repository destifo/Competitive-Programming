impl Solution {
    
    // O(n) time,
    // O(n) space,
    // Approach: string, 
    pub fn length_of_last_word(s: String) -> i32 {
        let words = s.split_whitespace();
        
        let mut last_word_len = 0;
        
        for word in words {
            last_word_len = word.len();
        }
        
        return last_word_len as i32;
    }
}