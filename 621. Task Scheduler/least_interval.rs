use std::collections::{BinaryHeap, VecDeque, HashMap};


impl Solution {
    
    // O(m) time, m -> len(tasks)
    // O(1) space,
    // Approach: heap, queue, greedy
    pub fn least_interval(tasks: Vec<char>, n: i32) -> i32 {
        let mut time = 0;
        let mut waiting: VecDeque<(i32, char)> = VecDeque::new();
        let mut heap = BinaryHeap::new();
        let mut count = HashMap::new();
        
        for task in &tasks {
            *count.entry(*task).or_insert(0) += 1;
        }
        
        for (task, t_count) in &count {
            heap.push((*t_count, *task));
        }
        
        
        while !heap.is_empty() || !waiting.is_empty() {
            if let Some((deqeue_time, task)) = waiting.front() {
                if time >= *deqeue_time {
                    let curr_count = count.get(task).unwrap();
                    heap.push((*curr_count, *task));
                    waiting.pop_front();
                } else if heap.is_empty() {
                    time = *deqeue_time;
                    let curr_count = count.get(task).unwrap();
                    heap.push((*curr_count, *task));
                    waiting.pop_front();
                }
            }
            
            time += 1;
            if let Some((task_count, task)) = heap.pop() {
                count.insert(task, task_count-1);
                if task_count-1 > 0 {
                    waiting.push_back((time+n, task));
                }
            }
        }
        
        time
    }
}