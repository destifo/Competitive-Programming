impl Solution {
    
    // O(n) time,
    // O(n) space,
    // Approach: mono stack, 
    pub fn daily_temperatures(temperatures: Vec<i32>) -> Vec<i32> {
        let temp_len = temperatures.len();
        let mut answer = vec![0;temp_len];
        let mut stack = Vec::new();
        
        for i in 0..temp_len {   
            while stack.len() > 0 && &temperatures[i] > &temperatures[stack[stack.len()-1]] {
                let popped = stack.pop().unwrap();
                answer[popped] = (i-popped) as i32;
            }
            stack.push(i);
        }
        
        return answer;
    }
}