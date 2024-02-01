impl Solution {
    
    // O(nlogn) timem,
    // O(n) space,
    // Approach: sorting, greedy
    pub fn divide_array(mut nums: Vec<i32>, k: i32) -> Vec<Vec<i32>> {
        /*
        
        1: sort the array, [1, 1, 3, 3, 4, 5, 7, 8, 9], [1, 2, 3, 3, 3, 7], [1, 1, 1, 3, 3, 3, 5, 5, 5,]
        2: create the buckets for the answer,
        3: check if the tuple of 3 seq are within k
        
        */
        
        let mut answer: Vec<Vec<i32>> = vec![vec![];nums.len()/3];
        
        nums.sort();
        for i in (0..nums.len()).step_by(3) {
            if nums[i+2]-nums[i] > k {
                return vec![];
            }
            for j in i..i+3 {
                answer[i/3].push(nums[j]);
            }
        }
        
        return answer;
    }
}