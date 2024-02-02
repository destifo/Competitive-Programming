

fn insertSeq(len: usize, lo: i32, hi: i32, answer: &mut Vec<i32>) {
    let digits = "123456789";
    
    for i in 0..digits.len()-len+1 {
        let num: i32 = digits[i..i+len].parse().unwrap();
        if num >= lo && num <= hi {
            answer.push(num);
        } else if num > hi {
            break;
        }
    }
}



impl Solution {
    
    // O(log(high)) time,
    // O(log(high)^2) space,
    // Approach: math, sliding window
    pub fn sequential_digits(low: i32, high: i32) -> Vec<i32> {
        let lo_len = (low as f64).log(10 as f64).ceil() as i32;
        let hi_len = (high as f64).log(10 as f64).ceil() as i32;
        
        let mut answer = vec![];
        for i in lo_len..hi_len+1 {
            insertSeq(i as usize, low, high, &mut answer);
        }
        
        answer
    }
}