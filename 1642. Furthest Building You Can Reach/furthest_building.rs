use std::collections::BinaryHeap;


impl Solution {
    
    // O(n) time,
    // O(bricks) space,
    // Approach: heap, greedy
    pub fn furthest_building(heights: Vec<i32>, mut bricks: i32, mut ladders: i32) -> i32 {
        let mut ans = 0;
        let mut heap: BinaryHeap<i32> = BinaryHeap::new();
        
        for i in 0..heights.len()-1 {
            if heights[i] >= heights[i+1] {
                ans = i+1;
                continue;
            } 

            // need to use resource
            let h_diff = heights[i+1]-heights[i];
            bricks -= h_diff;
            heap.push(h_diff);
            
            if bricks < 0 && ladders > 0 {
                if let Some(max_diff) = heap.pop() {
                    bricks += max_diff;
                }
                ladders -= 1;
            }
            
            if bricks < 0 {
                break;
            }
            ans = i+1;
        }
        
        ans as i32
    }
}