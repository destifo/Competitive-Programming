use std::cmp;
use std::collections::HashMap;
// use std::collections::tuple;

impl Solution {
    
    pub fn find_min_money(lo: i32, hi: i32, memo: &mut HashMap<(i32, i32), i32>) -> i32 {
        
        if (lo >= hi) {
            return 0;
        }
        
        if memo.contains_key(&(lo, hi)) {
            return *memo.get(&(lo, hi)).unwrap_or(&0);
        }
        
        let mut min_money = i32::MAX;
        
        for num in lo..hi+1 {
            
            let money = num + cmp::max(Solution::find_min_money(lo, num-1, memo), Solution::find_min_money(num+1, hi, memo));
            min_money = cmp::min(min_money, money);
            // println!("{}", money);
        }
        
        memo.insert((lo, hi), min_money);
        return min_money;
        
    }
    
    pub fn get_money_amount(n: i32) -> i32 {
        
        let mut memo = HashMap::new();
        
        return Solution::find_min_money(1, n, &mut memo);
        
    }
}