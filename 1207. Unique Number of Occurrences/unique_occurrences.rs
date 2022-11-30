use std::collections::{HashMap, HashSet};

impl Solution {
    
    // O(n) solution,
    // O(n) space,
    // Approach: hashtable, hashset
    pub fn unique_occurrences(arr: Vec<i32>) -> bool {
        
        let mut nums_count: HashMap<i32, i32> = HashMap::new();
        
        for num in arr {
            
            let mut count = 0;
            
            if nums_count.contains_key(&num) {
                count = *nums_count.get(&num).unwrap_or(&0);
            }
            
            count += 1;
            
            nums_count.insert(num, count);
        }
        
        let mut frequencies: HashSet<i32> = HashSet::new();
        
        for (num, count) in nums_count {
            if frequencies.contains(&count) {
                return false;
            }
            frequencies.insert(count);
        }
        
        return true;
    }
}