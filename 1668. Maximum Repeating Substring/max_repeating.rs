use std::cmp;


impl Solution {
    
    // O(n^2*word_len) time,
    // O(1) space,
    // Approach: string matching, brute force
    pub fn max_repeating(sequence: String, word: String) -> i32 {
        
        
        let mut max_k = 0;
        let word_len = word.len() as i32;
        let n: i32 = sequence.len() as i32;
        
        for j in 0..n {
            let mut i: i32 = j;
            let mut curr_k = 0;
            while i < n {
                let start: usize = i as usize;
                let end: usize = (i+word_len) as usize;

                if end > sequence.len() {
                    break;
                }

                let substring = &sequence[start..end];

                if substring == word {
                    curr_k += 1;
                    i +=word_len;
                }
                else {
                    max_k = cmp::max(max_k, curr_k);
                    curr_k = 0;
                    i += 1;
                }

            }

            max_k = cmp::max(max_k, curr_k);
        }
        
        
        return max_k;
    }
}