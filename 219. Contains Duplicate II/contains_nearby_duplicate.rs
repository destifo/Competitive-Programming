use std::collections::HashMap;

impl Solution {
    pub fn contains_nearby_duplicate(nums: Vec<i32>, k: i32) -> bool {
        
        let mut prev_index: HashMap<i32, i32> = HashMap::new();
        
        for i in 0..nums.len() {
            
            let num = nums[i];
            
            if prev_index.contains_key(&num) {
                
                let most_left: i32 = *prev_index.get(&num).unwrap_or(&0);
                let diff = i as i32 - most_left;
                
                if diff <= k {
                    return true;
                }
                
            }
            prev_index.insert(num, i as i32);
            
            
            
        }
        
        return false;
    }
}