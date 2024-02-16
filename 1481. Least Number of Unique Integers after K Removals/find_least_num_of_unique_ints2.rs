use std::collections::HashMap;


impl Solution {
    
    // O(klogn + n) time,
    // O(n) space,
    // Approach: sorting, hash map
    pub fn find_least_num_of_unique_ints(arr: Vec<i32>, mut k: i32) -> i32 {
        let mut count: HashMap<i32, i32> = HashMap::new();
        for num in arr {
            *count.entry(num).or_insert(0) += 1;
        }
        
        let mut sorted_count: Vec<(i32, i32)> = vec![];
        let mut ans = 0;
        for (num, cnt) in count {
            sorted_count.push((cnt, num));
            ans += 1;
        }
        sorted_count.sort();
        
        for (num_count, _) in sorted_count {
            if num_count > k {
                break;
            }
            k -= num_count;
            ans -= 1;
        }
        
        ans
    }
}