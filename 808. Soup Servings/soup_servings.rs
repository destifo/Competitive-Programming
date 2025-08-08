use std::collections::{VecDeque, HashMap};
use std::cmp::max;

struct Solution {}

impl Solution {
    pub fn calc_prob(a: i32, b: i32, memo: &mut HashMap<(i32, i32), f64>) -> f64 {
        if a == 0 && b == 0 {
            return 0.5;
        }

        if a == 0 {
            return 1.0;
        }

        if b == 0 {
            return 0.0;
        }

        let state = (a, b);
        if memo.contains_key(&state) {
            return *memo.get(&state).unwrap();
        }

        let mut prob = 0.0;
        let reductions = vec![
            (-100, 0), (-75, -25), 
            (-50, -50), (-25, -75)
            ];

        for (a_reduce, b_reduce) in &reductions {
            let a_new = a + a_reduce;
            let b_new = b + b_reduce;
            prob += 0.25 * Solution::calc_prob(max(a_new, 0), max(b_new, 0), memo);
        }
        memo.insert(state, prob);
        prob
    }

    pub fn soup_servings(n: i32) -> f64 {
        if n >= 5000 {
            return 1.0;
        }

        Solution::calc_prob(n, n, &mut HashMap::new())
    }
}