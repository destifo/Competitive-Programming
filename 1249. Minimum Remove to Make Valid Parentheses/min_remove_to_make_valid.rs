impl Solution {
    
    // O(n) time,
    // O(n) space,
    // Approach: stack, counting, 
    pub fn min_remove_to_make_valid(s: String) -> String {
        let mut diff = 0;
        let mut open = 0;
        let mut final_chars = vec![];
        
        for ch in s.chars() {
            match ch {
                '(' => {diff += 1; open += 1;},
                ')' => {
                    diff -= 1;
                    if diff < 0 {
                        diff += 1;
                        continue;
                    }
                },
                _ => (),
            }
            final_chars.push(ch)
        }
        
        let mut ans = String::new();
        for ch in final_chars {
            if ch == '(' {
                open -= 1;
                if open < diff {    
                    continue;
                }
            }
            ans.push(ch);
        }
        
        ans
    }
}