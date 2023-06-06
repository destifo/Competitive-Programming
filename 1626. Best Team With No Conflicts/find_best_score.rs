use std::cmp;
use std::collections::HashMap;

impl Solution {
    
    fn find_best_score(index: usize, max_score: i32, age_score: &Vec<(i32, i32)>, memo: &mut HashMap<(usize, i32), i32>) -> i32 {
        
        if index >= age_score.len() {
            return 0;
        }
        
        if memo.contains_key(&(index, max_score)) {
            return *memo.get(&(index, max_score)).unwrap();
        }
        
        let curr_age = age_score[index].0;
        let curr_score = age_score[index].1;
        
        let mut take_score = 0;
        
        if curr_score >= max_score {
            take_score = curr_score + Solution::find_best_score(index+1, curr_score, age_score, memo);
        }
        
        let mut skip_score = Solution::find_best_score(index+1, max_score, age_score, memo);
        
        memo.insert((index, max_score), cmp::max(take_score, skip_score));
        return cmp::max(take_score, skip_score);
    }
    
    
    // O(n^2) time,
    // O(n) space,
    // Approach: top down dp, sorting 
    pub fn best_team_score(scores: Vec<i32>, ages: Vec<i32>) -> i32 {
        let mut age_score = Vec::new();
        
        for i in 0..scores.len() {
            age_score.push((ages[i], scores[i]))
        }
        
        age_score.sort();
        
        let mut memo: HashMap<(usize, i32), i32> = HashMap::new();
        let ans = Solution::find_best_score(0 as usize, 0, &age_score, &mut memo);
        return ans;
    }
}