impl Solution {
    
    // O(n) time,
    // O(1) space,
    // Approach: math, 
    pub fn lexical_order(n: i32) -> Vec<i32> {
        let mut answer = Vec::new();
        answer.push(1);
        let mut num = 1;
        
        for i in 1..n {
            if num * 10 <= n {
                num *= 10;
            }
            else if num % 10 != 9 && num+1 <= n {
                num += 1;
            }
            else {
                while (num/10) % 10 == 9 {
                    num /= 10;
                }
                num = num/10 + 1;
            }
            answer.push(num)
        }
        
        return answer;
    }
}