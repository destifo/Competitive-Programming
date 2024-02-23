use std::collections::{VecDeque, HashMap};
use std::cmp::{min, Reverse};


impl Solution {
    
    // O(nlogn^2 + k) time,
    // O(n^2) space,
    // Approach: djikstra, heap, 
    pub fn find_cheapest_price(n: i32, flights: Vec<Vec<i32>>, src: i32, dst: i32, k: i32) -> i32 {
        let mut graph = vec![vec![];n as usize];
        
        for flight in flights {
            let from = flight[0];
            let to = flight[1];
            let price = flight[2];
            
            graph[from as usize].push((to, price));
        }
        
        let mut queue: VecDeque<(i32, i32)> = VecDeque::new();
        queue.push_back((src, 0));
        let mut min_cost = vec![i32::MAX;n as usize];
        min_cost[src as usize] = 0;
        
        for i in 0..=k {
            let queue_len = queue.len();
            for _ in 0..queue_len {
                let (city, tot_cost) = queue.pop_front().unwrap();
                
                for (nbr, price) in &graph[city as usize] {
                    if tot_cost + *price >= min_cost[*nbr as usize] {
                        continue
                    }
                    queue.push_back((*nbr, *price+tot_cost));
                    min_cost[*nbr as usize] = tot_cost + *price;
                }
            }
        }
        
        if min_cost[dst as usize] != i32::MAX {
            return min_cost[dst as usize];
        }
        
        -1
    }
}