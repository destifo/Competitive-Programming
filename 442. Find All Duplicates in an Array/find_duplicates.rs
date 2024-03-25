impl Solution {
    // O(n) time,
    // O(1) space,
    // Approach: in-place marking,
    pub fn find_duplicates(mut nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();

        let mut ans = vec![];
        for i in 0..n {
            let num = (nums[i].abs() - 1) as usize;
            if nums[num] < 0 {
                ans.push(num as i32 + 1);
            }
            nums[num] *= -1;
        }

        ans
    }
}
