impl Solution {
    
    pub fn collision_time(cars: &Vec<Vec<i32>>, curr: usize, next: usize) -> f64 {
        
        return (cars[next][0] - cars[curr][0]) as f64 / (cars[curr][1] - cars[next][1]) as f64
        
    }
    
    
    // O(n) time,
    // O(n) space,
    // Approach: monotonic stack, math, 
    pub fn get_collision_times(cars: Vec<Vec<i32>>) -> Vec<f64> {
        
        
        let mut stack: Vec<usize> = Vec::new();
        let mut collision_time = vec![-1 as f64; cars.len()];
        
        for i in (0..cars.len()).rev() {
            
            // println!("{}", i);
            while stack.len() > 0 && (cars[i][1] <= cars[stack[stack.len()-1]][1] || (stack.len() > 1 && Solution::collision_time(&cars, i, stack[stack.len()-1]) >= collision_time[stack[stack.len()-1]]) ) {
                stack.pop();
            }
            
            let time = if stack.len() == 0 {-1 as f64} else {Solution::collision_time(&cars, i, stack[stack.len()-1])};
            
            collision_time[i] = time;
            stack.push(i);
            
        }
        
        return collision_time;
        
    }
}