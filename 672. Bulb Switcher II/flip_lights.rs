use std::collections::{HashSet, VecDeque};

impl Solution {
    fn flip_bit(number: i32, position: u32) -> i32 {
        let mask = 1 << position;
        let flipped_number = number ^ mask;
        flipped_number
    }
    
    fn y_function(x: i32) -> i32 {
        3 * x + 1
    }
    
    fn get_neighbors(state: i32, n: i32) -> Vec<i32> {
        let mut nbrs: Vec<i32> = vec![];
        
        let mut curr_num = state;
        for i in 1..n {
            curr_num = Solution::flip_bit(curr_num, i as u32);
        }
        nbrs.push(curr_num);
            
        curr_num = state;
        for i in (1..n).step_by(2) {
            curr_num = Solution::flip_bit(curr_num, i as u32);
        }
        nbrs.push(curr_num);
            
        curr_num = state;
        for i in (0..n).step_by(2) {
            curr_num = Solution::flip_bit(curr_num, i as u32);
        }
        nbrs.push(curr_num);
        
        let mut i = 0;
        while Solution::y_function(i) < n {
            curr_num = Solution::flip_bit(curr_num, Solution::y_function(i) as u32);
            i += 1;
        }
        nbrs.push(curr_num);
        
        nbrs
    }
    
    // O(n*press) time,
    // O(n*space) space,
    // Approach: bfs, bit manipulation
    fn flip_lights(n: i32, presses: i32) -> i32 {
        let mut answer: HashSet<i32> = HashSet::new();
        let mut queue: VecDeque<i32> = VecDeque::new();
        queue.push_back((2_i32.pow(n as u32) - 1));
        answer.insert(queue[0]);
        
        let mut presses = presses;
        
        while presses > 0 && !queue.is_empty() {
            presses -= 1;
            let queue_len = queue.len();
            answer = HashSet::new();
            for _ in 0..queue_len {
                let state = queue.pop_front().unwrap();
                let nbrs = Solution::get_neighbors(state, n);
                for nbr in nbrs {
                    if answer.contains(&nbr) {
                        continue;
                    }
                    answer.insert(nbr);
                    queue.push_back(nbr);
                }
            }
        }

        answer.len() as i32
    }
}
