

fn count_nums_below_and_eq(nums: &Vec<i32>, target: i32) -> i32 {
    let mut count = 0;
    
    for num in nums {
        if *num <= target {
            count += 1;
        }
    }
    
    count
}


impl Solution {
    
    // O(nlogn) time,
    // O(1) space,
    // Approach: binary search, counting
    pub fn find_duplicate(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut ans = 1;
        let (mut low, mut high) = (1, n as i32);
        
        while low > 0 && low <= high {
            let mid = low + (high-low)/2;
            let below_eq_mid_count = count_nums_below_and_eq(&nums, mid);
            
            if below_eq_mid_count <= mid { // non repeated number
                low = mid+1;
            } else { // possible repeated number
                ans = mid;
                high = mid-1;
            }
        }
        
        ans 
    }
}