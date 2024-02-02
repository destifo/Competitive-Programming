use std::cmp::max;

fn update_minute(mins: &mut i32, mult: i32, inc: i32) -> i32 {
    *mins += mult*inc;
    
    *mins
}


impl Solution {
    
    // O(n) time,
    // O(1) space,
    // Approach: greedy, counting
    pub fn garbage_collection(garbage: Vec<String>, travel: Vec<i32>) -> i32 {
        let mut mins = 0;
        
        let mut g_mult = 0;
        let mut p_mult = 0;
        let mut m_mult = 0;
        
        for i in (0..garbage.len()).rev() {
            for t in garbage[i].chars() {
                match t {
                    'G' => {
                        g_mult = max(g_mult, 1);
                        update_minute(&mut mins, g_mult, 1);
                    },
                    'P' => {
                        p_mult = max(p_mult, 1);
                        update_minute(&mut mins, p_mult, 1);
                    },
                    'M' => {
                        m_mult = max(m_mult, 1);
                        update_minute(&mut mins, m_mult, 1);
                    },
                    _ => {}
                }
            }
            
            if i > 0 {
                update_minute(&mut mins, g_mult, travel[i-1]);
                update_minute(&mut mins, p_mult, travel[i-1]);
                update_minute(&mut mins, m_mult, travel[i-1]);
            }
        }
        
        mins
    }
}