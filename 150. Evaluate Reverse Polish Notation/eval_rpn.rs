impl Solution {
    
    // O(n) time,
    // O(n) space,
    // Approach: stack, math
    pub fn eval_rpn(tokens: Vec<String>) -> i32 {
        
        let mut stack: Vec<i32> = Vec::new();
        
        for token in tokens {
            
            if token.parse::<i32>().is_ok() {
                stack.push(token.parse::<i32>().unwrap());
            }
            else {
                let val1 = stack.pop().unwrap();
                let val2 = stack.pop().unwrap();
                
                if token == "+" {
                    stack.push(val1+val2);
                }
                else if token == "-" {
                    stack.push(val2-val1);
                }
                else if token == "*" {
                    stack.push(val1*val2);
                }
                else {
                    stack.push(val2/val1);
                }
            }
            
        }
        
        return stack[0];
    }
}