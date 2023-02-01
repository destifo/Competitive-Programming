use std::cmp;


impl Solution {
    pub fn minimum_recolors(blocks: String, k: i32) -> i32 {
        let mut left = 0;
        let mut right = k as usize;
        
        let mut white_count = 0;
        let mut black_count = 0;
        let mut chrs = Vec::new();
        for ch in blocks.chars() {
            chrs.push(ch);
        }
        
        for i in 0..right {
            if chrs[i] == 'W' {
                white_count += 1;
            } else {
                black_count += 1;
            }
        }
        
        let mut min_ops = white_count;
        while right < blocks.len() {
            if chrs[left] == 'W' { white_count -= 1 } else { black_count -= 1 }
            left += 1;
            if chrs[right] == 'W' { white_count += 1 } else { black_count += 1 }
            right += 1;
            min_ops = cmp::min(min_ops, white_count); 
        }
        
        return min_ops;
    }
}