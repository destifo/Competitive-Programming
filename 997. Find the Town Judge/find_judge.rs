impl Solution {
    
    // O(n + m) time, m -> len(trust)
    // O(n) space,
    // Approach: graph, 
    pub fn find_judge(n: i32, trust: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let mut incoming = vec![0;n+1];
        let mut outgoing = vec![0;n+1];
        
        for t in trust {
            let a = t[0];
            let b = t[1];
            outgoing[a as usize] += 1;
            incoming[b as usize] += 1;
        }

        for person in 1..=n {
            if incoming[person] == (n as i32-1) && outgoing[person] == 0 {
                return person as i32;
            }
        }
        
        -1
    }
}