use std::collections::HashMap;

impl Solution {
    
    fn getPairs(val: i32, count: &HashMap<i32, i32>) -> i64 {
        
        let mut answer = 0 as i64;
        
        for i in (0..22) {
            let power_of_two = i32::pow(2, i);
            let target = power_of_two - val;
            
            if count.contains_key(&target) {
                let target_count = *count.get(&target).unwrap() as i64;
                answer += if (target == val) {target_count-1} else {target_count};
            }   
        }
        return answer;
    }
    
    
    // O(n) time,
    // O(n) space,
    // Approach: hashmap, 
    pub fn count_pairs(deliciousness: Vec<i32>) -> i32 {
        let mut nums_count: HashMap<i32, i32> = HashMap::new();
        for num in &deliciousness {
            let mut count = 0;
            if nums_count.contains_key(&num) {
                count = *nums_count.get(&num).unwrap();
            }
            count += 1;
            nums_count.insert(*num, count);
        }
        
        let mut answer = 0;
        for num in deliciousness {
            answer += Solution::getPairs(num, &nums_count);
        }
        answer /= 2;
        let MOD = i64::pow(10, 9) + 7;
        answer %= MOD;
        return answer as i32;
    }
}