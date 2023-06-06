impl Solution {
    
    fn count_less_or_equal_target(target: i32, arr: &Vec<i32>) -> i32 {
        
        let mut lo = 0;
        let mut hi = arr.len()-1;
        let mut ans = arr.len();
        
        while hi <= arr.len() && lo <= hi {
            let mid = lo + (hi-lo)/2;
            if arr[mid] > target {
                ans = mid;
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }
        
        return ans as i32;
    }
    
    
    // O(logn squared) time,
    // O(1) space,
    // Approach: binary search, 
    pub fn find_kth_positive(arr: Vec<i32>, k: i32) -> i32 {
        
        let mut lo = 1;
        let mut hi = arr[arr.len()-1]+k;
        let mut ans = 1;
        
        while lo <= hi {
            let mid = lo + (hi-lo)/2;
            let less_count = Solution::count_less_or_equal_target(mid, &arr);
            if k + less_count == mid {
                ans = mid;
                hi = mid-1;
            } else if k + less_count > mid {
                lo = mid+1;
            } else {
                hi = mid-1;
            }
        }
        
        return ans;
    }
}