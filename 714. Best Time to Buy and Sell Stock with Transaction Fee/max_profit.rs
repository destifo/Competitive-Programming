use std::cmp;
use std::collections::HashMap;

impl Solution {
    
    pub fn make_transaction(index: usize, buying: bool, prices: &Vec<i32>, fee: i32, memo: &mut HashMap<(usize, bool), i32>) -> i32 {
        
        if index >= prices.len() {
            return 0;
        }
        
        if memo.contains_key(&(index, buying)) {
            return *memo.get(&(index, buying)).unwrap();
        }
        
        if buying {
            let buy = -prices[index] - fee + Solution::make_transaction(index+1, !buying, prices, fee, memo);
            let skip_buying = Solution::make_transaction(index+1, buying, prices, fee, memo);
            
            memo.insert((index, buying), cmp::max(buy, skip_buying));
            return cmp::max(buy, skip_buying);
        }
        else {
            let sell = prices[index] + Solution::make_transaction(index+1, !buying, prices, fee, memo);
            let skip_sell = Solution::make_transaction(index+1, buying, prices, fee, memo);
            
            memo.insert((index, buying), cmp::max(sell, skip_sell));
            return cmp::max(sell, skip_sell);
        }
        
    }
    
    
    // O(n) time,
    // O(n) space,
    // Approach: dp, top down
    pub fn max_profit(prices: Vec<i32>, fee: i32) -> i32 {
        Solution::make_transaction(0 as usize, true, &prices, fee, &mut HashMap::new())
    }
}