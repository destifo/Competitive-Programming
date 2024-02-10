

fn find_even_len_pali(i: usize, s: &Vec<char>) -> i32 {
    let mut count = 0;
    let (mut left, mut right) = (i, i+1);
    
    while right < s.len() {
        if s[left] != s[right] {
            break;
        }
        count += 1;
        if left == 0 {
            break;
        }
        left -= 1;
        right += 1;
    }
    
    count
}


fn find_odd_len_pali(i: usize, s: &Vec<char>) -> i32 {
    let mut count = 1;
    if i == 0 {
        return count;
    }
    let (mut left, mut right) = (i-1, i+1);
    
    while right < s.len() {
        if s[left] != s[right] {
            break;
        }
        count += 1;
        if left == 0 {
            break;
        }
        left -= 1;
        right += 1;
    }
    
    count
}


impl Solution {
    
    // O(n^2) time,
    // O(1) space,
    // Approach: string, iteration, 
    pub fn count_substrings(s: String) -> i32 {
        let mut ans = 0;
        let n = s.len();
        let chars: Vec<char> = s.chars().collect();
        
        for i in 0..n {
            ans += find_even_len_pali(i, &chars);
            ans += find_odd_len_pali(i, &chars);
        }
        
        ans
    }
}