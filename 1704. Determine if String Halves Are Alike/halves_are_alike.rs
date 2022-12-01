use std::collections::{HashSet, HashMap};
use std::iter::FromIterator;

impl Solution {
    
    // O(n) time,
    // O(1) space,
    // Approach: string, array, counting
    pub fn halves_are_alike(s: String) -> bool {
        
        let v = [ 'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u' ];
        
        let vowels: HashSet<&char> = HashSet::from_iter(v.iter());
        let mut vowel_sum = 0;
        
        let mid = s.len()/2;
        
        for (i, ch) in s.chars().enumerate() {            
            if !vowels.contains(&ch) {
                continue;
            }
            
            if i < mid {
                vowel_sum += 1;
            }
            else {
                vowel_sum -=1;
            }
        }
        
        return vowel_sum == 0;
    }
}