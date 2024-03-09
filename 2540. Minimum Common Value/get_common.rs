impl Solution {
    
    // O(n + m) time,
    // O(1) space,
    // Approach: two pointers, 
    pub fn get_common(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let (mut p1, mut p2) = (0, 0);
        
        while p1 < nums1.len() && p2 < nums2.len() {            
            if nums1[p1] < nums2[p2] {
                p1 += 1;
            }
            else if nums1[p1] > nums2[p2] {
                p2 += 1;
            } else {
                return nums1[p1];
            }
        }
        
        -1
    }
}