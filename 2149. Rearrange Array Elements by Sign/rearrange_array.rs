
impl Solution {
    
    // O(n) time,
    // O(1) space,
    // Approach: two pointers, 
    pub fn rearrange_array(nums: Vec<i32>) -> Vec<i32> {
        let mut positives: Vec<i32> = vec![];
        let mut negatives: Vec<i32> = vec![];
        let n = nums.len();
        
        for num in nums {
            if num > 0 {
                positives.push(num);
            } else {
                negatives.push(num);
            }
        }
        
        let mut answer = vec![0;n];
        let (mut p_index, mut n_index) = (0, 0);
        for i in 0..n {
            if i % 2 == 0 {
                answer[i] = positives[p_index];
                p_index += 1;
            } else {
                answer[i] = negatives[n_index];
                n_index += 1;
            }
        }
        
        answer
    }
}