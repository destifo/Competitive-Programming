fn get_greatest_below_sum(low: usize, sum: i32, nums: &Vec<i32>) -> usize {
    let mut low = low;
    let mut hi = nums.len()-1;
    let mut index = low-1;
    
    while low <= hi {
        let mid = (low + hi)/2;
        if nums[mid] >= sum {
            hi = mid-1;
        } else {
            index = mid;
            low = mid+1;
        }
    }
    
    index
}


impl Solution {
    
    // O(n^2logn) time,
    // O(1) space,
    // Approach: sorting, binary search
    pub fn triangle_number(nums: Vec<i32>) -> i32 {
        let mut ans = 0;
        let n = nums.len();
        
        if n < 3 {
            return ans;
        }
        
        let mut nums = nums;
        nums.sort();
        
        for i in 0..n-2 {
            let num1 = nums[i];
            for j in i+1..n-1 {
                let num2 = nums[j];
                let sum = num1 + num2;
                let index = get_greatest_below_sum(j+1, sum, &nums);
                let thirds = index - j;
                ans += thirds as i32;
            }
        }
        
        ans
    }
}