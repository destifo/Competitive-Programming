use std::cmp;

impl Solution {
    
    pub fn find_total_time(node: i32, graph: &Vec<Vec<i32>>, time: &Vec<i32>) -> i32 {
        
        let mut max_time = 0;
        
        for emp in &graph[node as usize] {
            
            max_time = cmp::max(max_time, Solution::find_total_time(*emp, graph, time));
            
        }
        
        return time[node as usize] + max_time;
        
    }
    
    
    // O(n) time,
    // O(n) space,
    // Approach: dfs, recursion
    pub fn num_of_minutes(n: i32, head_id: i32, manager: Vec<i32>, inform_time: Vec<i32>) -> i32 {
        
        let mut graph = vec![Vec::new();n as usize];
        
        for (emp, boss) in manager.iter().enumerate() {
            if *boss == -1 {
                continue;
            }
            
            let index = *boss;
            graph[index as usize].push(emp as i32);
        }
        
        return Solution::find_total_time(head_id, &graph, &inform_time);
    }
}