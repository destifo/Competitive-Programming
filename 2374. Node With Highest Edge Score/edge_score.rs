impl Solution {
    
    // O(n) time,
    // O(n) space,
    // Approach: counting, graph
    pub fn edge_score(edges: Vec<i32>) -> i32 {
        
        let mut incomings: Vec<i64> = vec![0;edges.len()];
        
        for (start, end) in edges.iter().enumerate() {
            incomings[*end as usize] += start as i64;
        }
        
        let mut answer = 0 as usize;
        let mut max_score = 0;
        
        for (node, score) in (&incomings).iter().enumerate().rev() {
            if *score >= max_score {
                max_score = *score ;
                answer = node;
            }
        }

        return answer as i32;
    }
}