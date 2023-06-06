use std::cmp;
use std::collections::HashMap;

impl Solution {
    
    pub fn find_min_squares(remaining: i32, memo: &mut HashMap<i32, i32>) -> i32 {
        
        if memo.contains_key(&remaining) {
            return *memo.get(&remaining).unwrap_or(&0);
        }
        
        if remaining == 0 {
            return 0;
        }
        
        let mut min_squares = i32::MAX;
        for i in 1..remaining+1 {
            
            let square = (i*i);
            
            if square > remaining{
                break;
            }
            
            let answer = 1 + Solution::find_min_squares(remaining-square, memo);
            min_squares = cmp::min(min_squares, answer);
        }
        
        memo.insert(remaining, min_squares);
        return min_squares;
        
    }
    
    
    // O(n) time,
    // O(n) space,
    // Approach: dp with memoization,
    pub fn num_squares(n: i32) -> i32 {
        
        let mut memo = HashMap::new();
        return Solution::find_min_squares(n, &mut memo);
        
    }


    // O(n) time,
    // O(n) space,
    // Approach: bottom up dp, 
    pub fn num_squares2(n: i32) -> i32 {
        
        let size = (n+1) as usize;
        let mut min_squares: Vec<i32> = vec![i32::MAX; size]; 
        
        min_squares[1 as usize] = 1;
        min_squares[0 as usize] = 0;
        
        for i in 2..n+1 {
            
            for root in 1..i {
                
                let square = root*root;
                
                if square > i {
                    break;
                }
                
                min_squares[i as usize] = cmp::min(min_squares[i as usize], 1+min_squares[(i-square) as usize]);
                
            }
            
        }
        
        return min_squares[n as usize];
    }

    
    // Approach: bfs, 
    pub fn num_squares(n: i32) -> i32 {
        
        let mut queue: VecDeque<i32> = VecDeque::new();
        let mut visited = HashSet::new(); 
        
        for root in 1..n+1 {
            let square = root*root;
            
            if square > n {
                break;
            }
            
            queue.push_back(n-square);
            visited.insert(n-square);
        }
        
        let mut depth = 0;
        
        while queue.len() > 0 {
            
            depth += 1;
            let queue_len = queue.len();
            
            for i in 0..queue_len {
                
                let val = queue.pop_front().unwrap_or(0);
                
                if val == 0 {
                    return depth;
                }
                
                for root in 1..val+1 {
                    let square = root*root;

                    if square > val {
                        break;
                    }
                    
                    if visited.contains(&(val-square)) {
                        continue;
                    }

                    queue.push_back(val-square);
                    visited.insert(val-square);
                }
            }
        }
        
        return -1;
        
    }
}