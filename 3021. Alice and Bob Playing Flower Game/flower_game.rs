fn count_odds_below_num(num: i32) -> i64 {
    (num as i64 +1) / 2
}

fn count_evens_below_num(num: i32) -> i64 {
    num as i64 / 2
}

impl Solution {

    // O(1) time,
    // O(1) space,
    // Approach: math, 
    pub fn flower_game(n: i32, m: i32) -> i64 {
        (count_evens_below_num(n) * count_odds_below_num(m)) + 
        (count_evens_below_num(m) * count_odds_below_num(n))
    }
}
