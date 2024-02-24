use std::cmp::Reverse;
use std::collections::{BinaryHeap, HashMap, HashSet, VecDeque};


fn bfs(p: usize, graph: &HashMap<usize, Vec<usize>>, has_secret: &mut Vec<bool>) {
    if !graph.contains_key(&p) {
        return;
    }
    let mut queue: VecDeque<usize> = VecDeque::new();
    queue.push_back(p);

    while !queue.is_empty() {
        let queue_len = queue.len();
        for _ in 0..queue_len {
            let person = queue.pop_front().unwrap();
            for nbr in &graph[&person] {
                if has_secret[*nbr] {
                    continue;
                }
                has_secret[*nbr] = true;
                queue.push_back(*nbr);
            }
        }
    }
}


impl Solution {
    
    // O(mlogm + n) time, m -> len(meetings),
    // O(m + n) space,
    // Approach: heap, hash map, bfs
    pub fn find_all_people(n: i32, meetings: Vec<Vec<i32>>, first_person: i32) -> Vec<i32> {
        let mut has_secret = vec![false;n as usize];
        has_secret[0] = true;
        has_secret[first_person as usize] = true;
        
        let mut heap: BinaryHeap<Reverse<(i32, usize, usize)>> = BinaryHeap::new();
        for meeting in meetings {
            let [person1, person2, time] = meeting.as_slice() else { todo!()};
            heap.push(Reverse((*time, *person1 as usize, *person2 as usize)));
        }
        
        let mut prev_time = -1;
        let mut graph: HashMap<usize, Vec<usize>> = HashMap::new();
        let mut curr_with_secrets: HashSet<usize> = HashSet::new();
        while !heap.is_empty() {
            let Reverse((time, person1, person2)) = heap.pop().unwrap();
            if time != prev_time {
                for p in &curr_with_secrets {
                    bfs(*p, &graph, &mut has_secret);
                }
                curr_with_secrets = HashSet::new();
                graph = HashMap::new();
                prev_time = time;
            }
            if has_secret[person1] && has_secret[person2] {
                continue;
            }
            if !has_secret[person1] && !has_secret[person2] {
                graph.entry(person1).or_insert(vec![]).push(person2);
                graph.entry(person2).or_insert(vec![]).push(person1);
                continue;
            }
            has_secret[person1] = true;
            has_secret[person2] = true;
            curr_with_secrets.insert(person1);
            curr_with_secrets.insert(person2);
        }
        
        for p in &curr_with_secrets {
            bfs(*p, &graph, &mut has_secret);
        }
        
        let mut ans = vec![];
        for (person, secret) in has_secret.iter().enumerate() {
            if *secret {
                ans.push(person as i32);
            }
        }
        
        ans
    }
}