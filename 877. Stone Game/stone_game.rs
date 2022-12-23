use std::cmp;
use std::collections::HashMap;


impl Solution {
    
    fn min_max(alice: bool, start: usize, end: usize, piles: &Vec<i32>, memo: &mut HashMap<(usize, usize), i32>) -> i32 {
        if start > end || end >= piles.len() {
            return 0;
        }
        
        if memo.contains_key(&(start, end)) {
            return *memo.get(&(start, end)).unwrap();
        }

        let mut ans = 0;
        if alice {
            let left = Solution::min_max(!alice, start+1, end, piles, memo) + piles[start];
            let right = Solution::min_max(!alice, start, end-1, piles, memo) + piles[end];

            ans = cmp::max(left, right);
        } else {
            let left = Solution::min_max(!alice, start+1, end, piles, memo) - piles[start];
            let right = Solution::min_max(!alice, start, end-1, piles, memo) - piles[end];

            ans = cmp::min(left, right);
        }
        
        memo.insert((start, end), ans);
        return ans;
    }
    
    pub fn stone_game(piles: Vec<i32>) -> bool {
        let mut memo: HashMap<(usize, usize), i32> = HashMap::new();
        let max_for_alice = Solution::min_max(true, 0 as usize, piles.len() as usize-1, &piles, &mut memo);
        if max_for_alice > 0 {
            return true;
        }
        return false;
    }


    // O(1) time,
    // O(1) space,
    // Approach: logical thinking, 
    pub fn stone_game(piles: Vec<i32>) -> bool {
        return true;
    }
}