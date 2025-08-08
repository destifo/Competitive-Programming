use std::collections::HashMap;
use std::hash::Hash;

trait ToFrequencyMap {
    type Item;

    fn to_map(&self) -> HashMap<Self::Item, i32>
    where 
        Self::Item: Eq + Hash + Copy;
}

impl<T> ToFrequencyMap for Vec<T> where T: Eq + Hash + Copy {
    type Item = T;

    fn to_map(&self) -> HashMap<T, i32> {
        let mut count = HashMap::new();
        for item in self {
            *count.entry(*item).or_insert(0) += 1;
        }

        count
    }
}

struct FindSumPairs {
    nums2: Vec<i32>,
    nums1_count: HashMap<i32, i32>,
    nums2_count: HashMap<i32, i32>
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */

/**
* O((n * c) + m) time, n -> len(nums1), c -> amount of time add and count are called, precisely though, n is the no of unique elts in nums1
* O(n + m) space, m -> len(nums2)
* Approach: counting, hashmap
*/
impl FindSumPairs {

    fn new(nums1: Vec<i32>, nums2: Vec<i32>) -> Self {
        let nums2_count = nums2.to_map();
        Self {
            nums2,
            nums1_count: nums1.to_map(),
            nums2_count
        }
    }
    
    fn add(&mut self, index: i32, val: i32) {
        let num = self.nums2[index as usize];
        let new_val = num + val;

        self.nums2[index as usize] += val;
        if let Some(num_count) = self.nums2_count.get_mut(&num) {
            *num_count -= 1;
        }
        *self.nums2_count.entry(new_val).or_insert(0) += 1;
    }
    
    fn count(&self, tot: i32) -> i32 {
        let mut ans = 0;
        for (num, count) in self.nums1_count.iter() {
            let target = tot - *num;
            if let Some(target_count) = self.nums2_count.get(&target) {
                let tot_comb = *target_count * *count;
                ans += tot_comb;
            }
        } 

        ans
    }
}

/**
 * Your FindSumPairs object will be instantiated and called as such:
 * let obj = FindSumPairs::new(nums1, nums2);
 * obj.add(index, val);
 * let ret_2: i32 = obj.count(tot);
 */
