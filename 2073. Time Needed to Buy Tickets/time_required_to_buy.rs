use std::cmp::min;

impl Solution {
    // O(n) time,
    // O(1) space,
    // Approach: array,
    pub fn time_required_to_buy(tickets: Vec<i32>, k: i32) -> i32 {
        let mut time = 0;
        let rounds = tickets[k as usize];
        let n = tickets.len();

        for i in 0..n {
            if i <= k as usize {
                let rounds_before_leaving = min(rounds, tickets[i]);
                time += rounds_before_leaving;
            } else {
                let rounds_before_leaving = min(rounds - 1, tickets[i]);
                time += rounds_before_leaving;
            }
        }

        time
    }
}
