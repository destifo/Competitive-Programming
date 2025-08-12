use std::collections::HashMap;

impl Solution {

    pub fn count(n: i32, x: i32, curr_num: i32, memo: &mut HashMap<(i32, i32), i32>) -> i32 {
        if n == 0 {
            return 1;
        }

        if n < 0 || curr_num > n {
            return 0;
        }

        let state = (n, curr_num);
        if memo.contains_key(&state) {
            return memo[&state];
        }

        let mut ans = 0;
        let power = curr_num.pow(x as u32);
        if power > 0 && power <= n {
            ans += Solution::count(n-power, x, curr_num+1, memo);
        }
        ans += Solution::count(n, x, curr_num+1, memo);
        let MOD = 10_i32.pow(9) + 7;
        ans %= MOD;

        memo.insert(state, ans);
        ans
    }

    // O(n^2) time,
    // O(n^2) time,
    // Approach: bottom-up dp, memoization
    pub fn number_of_ways(n: i32, x: i32) -> i32 {
        Solution::count(n, x, 1, &mut HashMap::new()) 
    }
}
