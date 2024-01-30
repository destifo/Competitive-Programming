use std::collections::HashSet;

impl Solution {
    
    pub fn calc(num1: i32, num2: i32, op: &str) -> i32 {
        match op {
            "+" => num1 + num2,
            "*" => num1 * num2,
            "-" => num1 - num2,
            _ => num1 / num2
        }
    }
    
    pub fn eval_rpn(tokens: Vec<String>) -> i32 {
        let mut stack: Vec<i32> = vec![];
        let ops_vec = vec![ '+', '*', '-', '/'];
        let ops: HashSet<String> = ops_vec.into_iter().map(|s| s.to_string()).collect();
        
        for token in tokens {
            if ops.contains(&token.to_string()) {
                let num2: i32 = stack.pop().unwrap();
                let num1: i32 = stack.pop().unwrap();
                stack.push(Solution::calc(num1, num2, &token));
            } else {
                stack.push(token.parse::<i32>().unwrap());
            }
        }
        
        stack.pop().unwrap()
    }
}