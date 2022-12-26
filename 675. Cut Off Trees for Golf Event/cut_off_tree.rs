use std::collections::{BinaryHeap, VecDeque, HashSet};


impl Solution {
    
    fn in_bounds(x: i32, y: i32, rows: i32, cols: i32) -> bool {
        if x < 0 || x >= rows || y < 0 || y >= cols {
            return false;
        }
        return true;
    }
    
    fn get_neighbors(row: i32, col: i32, forest: &Vec<Vec<i32>>) -> Vec<(usize, usize)> {
        let mut neighbors: Vec<(usize, usize)> = Vec::new();
        let ROWS = forest.len() as i32;
        let COLS = forest[0].len() as i32;
        let directions = [(0, 1), (0, -1), (1, 0), (-1, 0)];
        
        for (x0, y0) in directions {
            
            let x = row + x0;
            let y = col + y0;
            
            if Solution::in_bounds(x, y, ROWS, COLS) && forest[x as usize][y as usize] > 0 {
                neighbors.push((x as usize, y as usize));
            }
        }
        
        return neighbors; 
    }
    
    fn find_min_dist(start_row: usize, start_col: usize, target_row: usize, target_col: usize, forest: &Vec<Vec<i32>>) -> i32 {
        
        let mut depth = 0;
        let mut visited: HashSet<(usize, usize)> = HashSet::new();
        
        let mut queue = VecDeque::new();
        queue.push_front((start_row, start_col));
        visited.insert((start_row, start_col));
        
        while queue.len() > 0 {
            let queue_len = queue.len();
            
            for i in 0..queue_len {
                let coord = queue.pop_front().unwrap();
                let curr_row = coord.0;
                let curr_col = coord.1;
                
                if curr_row == target_row && curr_col == target_col {
                    return depth;
                }
                
                for nbr in Solution::get_neighbors(curr_row as i32, curr_col as i32, forest) {
                    if visited.contains(&nbr) {
                        continue;
                    }
                    visited.insert(nbr);
                    queue.push_back(nbr);
                }  
            } 
            depth += 1;
        }
        
        return -1;
    }
    
    
    // O((m*n)^2 + m*nlogm*n) time,
    // O(m*n) space,
    // Approach: bfs, heap, 
    pub fn cut_off_tree(forest: Vec<Vec<i32>>) -> i32 {
        
        if forest[0][0] == 0 {
            return -1;
        }
        
        let mut heap = BinaryHeap::new();
        heap.push((-forest[0][0], 0, 0));
        for row in 0..forest.len() {
            for col in 0..forest[0].len() {
                if forest[row][col] < 2 || (row == 0 && col == 0) {
                    continue;
                }
                heap.push((-forest[row][col], row, col));
            }
        }
        
        let mut steps = 0;
        if heap.len() > 0 {
            let next = heap.peek().unwrap();
            let short_dist = Solution::find_min_dist(0, 0, next.1, next.2, &forest);
            if short_dist == -1 {
                return -1;
            }
            steps += short_dist;
        }
        
        while heap.len() > 1 {
            let cell = heap.pop().unwrap();
            let next = heap.peek().unwrap();
            let short_dist = Solution::find_min_dist(cell.1, cell.2, next.1, next.2, &forest);
            if short_dist == -1 {
                return -1;
            }
            steps += short_dist;
        }
        
        return steps;
    }
}