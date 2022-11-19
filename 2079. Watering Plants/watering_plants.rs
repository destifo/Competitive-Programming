impl Solution {
    
    // O(n) time,
    // O(n) space,
    // Approach: array, math
    pub fn watering_plants(plants: Vec<i32>, capacity: i32) -> i32 {
       
        let mut checkpoints: Vec<i32> = Vec::new();
        
        let mut curr_filled = 0;
        
        for i in 0..plants.len() {
            
            let curr_needed = plants[i];
            
            if curr_needed + curr_filled > capacity {
                curr_filled = curr_needed;
                checkpoints.push((i-1) as i32);
            }
            else {
                curr_filled += curr_needed;
            }
            
        }
        
        let mut steps: i32 = 0;
        
        for checkpoint in &checkpoints {
            
            steps += 2*(checkpoint+1);
            
        }
        steps += plants.len() as i32;
        
        return steps;
        
    }
}