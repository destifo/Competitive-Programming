fn is_pali(s: Vec<char>) -> bool {
    let (mut left, mut right) = (0, s.len()-1);
    
    while left < right {
        if s[left] != s[right] {
            return false;
        }
        left += 1;
        right -= 1;
    }
    
    true
}


impl Solution {
    
    // O(n) time, n -> sum(all the words)
    // O(n) space,
    // Approach: two pointers, 
    pub fn first_palindrome(words: Vec<String>) -> String {
        for word in words {
            if is_pali(word.chars().collect()) {
                return word;
            }
        }
        
        "".to_string()
    }
}