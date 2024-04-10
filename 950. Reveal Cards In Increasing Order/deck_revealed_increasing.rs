use std::collections::VecDeque;

impl Solution {
    // O(n) time,
    // O(n) space,
    // Approach: reverse engineering, simulation, queue
    pub fn deck_revealed_increasing(mut deck: Vec<i32>) -> Vec<i32> {
        deck.sort();
        let mut queue = VecDeque::new();

        while !deck.is_empty() {
            let num = deck.pop().unwrap();
            if queue.len() > 1 {
                let last = queue.pop_back().unwrap();
                queue.push_front(last);
            }
            queue.push_front(num);
        }

        let ans: Vec<i32> = queue.into_iter().collect();
        ans
    }
}
