use std::collections::{HashMap};


impl Solution {
    
    pub fn check(index: usize, stack: &mut Vec<char>, string: &Vec<char>, memo: &mut HashMap<(usize, usize), bool>) -> bool {
        
        if index >= string.len() {
            return stack.len() == 0;
        }
        
        if memo.contains_key(&(index, stack.len())) {
            return *memo.get(&(index, stack.len())).unwrap();
        }
        
        let curr_char = string[index];
        let mut ans = false;
        if curr_char == '(' {
            stack.push('(');
            if Solution::check(index+1, stack, string, memo) {
                memo.insert((index, stack.len()-1), true);
                return true;
            }
            stack.pop();
        }
        else if curr_char == ')' {
            if stack.len() > 0 {
                stack.pop();
                if Solution::check(index+1, stack, string, memo) {
                    memo.insert((index, stack.len()+1), true);
                    return true;
                }
                stack.push('(');
            }
        }
        else {
            if Solution::check(index+1, stack, string, memo) {
                memo.insert((index, stack.len()), true);
                return true;
            }
            
            stack.push('(');
            if Solution::check(index+1, stack, string, memo) {
                memo.insert((index, stack.len()-1), true);
                return true;
            }
            stack.pop();
            
            if stack.len() > 0 {
                stack.pop();
                if Solution::check(index+1, stack, string, memo) {
                    memo.insert((index, stack.len()+1), true);
                    return true;
                }
                stack.push('(');
            }
        }
        
        memo.insert((index, stack.len()), false);
        return false;
    }
    
    
    // O(n) time, 
    // O(n^2) space,
    // Approach: dp, top down, memoization, stack
    pub fn check_valid_string(s: String) -> bool {
        let chars = s.chars().collect();
        return Solution::check(0, &mut Vec::new(), &chars, &mut HashMap::new());
    }
}