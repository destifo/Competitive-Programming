impl Solution {
    // O(n) time,
    // O(1) space,
    // Approach: sliding window
    pub fn num_subarray_product_less_than_k(nums: Vec<i32>, k: i32) -> i32 {
        if k <= 1 {
            return 0;
        }

        let n = nums.len();
        let (mut left, mut right) = (0, 0);
        let mut prod = 1;
        let mut ans = 0;

        while right < n {
            prod *= nums[right];

            while prod >= k {
                prod /= nums[left];
                left += 1;
            }
            right += 1;
            ans += (right - left) as i32;
        }

        ans
    }
}
