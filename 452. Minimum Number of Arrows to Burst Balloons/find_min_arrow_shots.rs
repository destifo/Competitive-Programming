use std::cmp;


impl Solution {
    
    // O(nlogn) time,
    // O(1) space,
    // Approach: sorting, greedy, 
    pub fn find_min_arrow_shots(mut points: Vec<Vec<i32>>) -> i32 {
        points.sort();
        let mut last_limit = points[0][1];
        let mut arrows = 1;
        
        for point in points {
            let start = point[0];
            let end = point[1];
            if start <= last_limit {
                last_limit = cmp::min(last_limit, end);
            } else {
                last_limit = end;
                arrows += 1
            }
        }
        
        return arrows;
    }
}