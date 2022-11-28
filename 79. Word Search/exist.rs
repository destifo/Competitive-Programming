use std::collections::HashSet;

impl Solution {
    
    pub fn in_bounds(row: usize, col: usize, board: &Vec<Vec<char>>) -> bool {
        
        if row >= board.len() {
            return false;
        }
        
        if col >= board[0].len() {
            return false;
        }
        
        return true;
    }
    
    
    pub fn get_neighbors(board: &Vec<Vec<char>>, row: usize, col: usize) -> Vec<Vec<usize>> {
        
        let mut neighbors = Vec::new();
        
        let directions = [[0, 1], [0, -1], [1, 0], [-1, 0]];
        
        for direction in directions {
            let new_row = (row as i32+direction[0]) as usize;
            let new_col = (col as i32+direction[1]) as usize;
            if Solution::in_bounds(new_row, new_col, board) {
                neighbors.push(vec![new_row, new_col]);
            }
        }
        
        return neighbors;
        
    }
    
    
    pub fn find_word(index: usize, row: usize, col: usize, board: &Vec<Vec<char>>, word: &Vec<char>, visited: &mut HashSet<(usize, usize)>) -> bool {
        
        if board[row][col] != word[index] || visited.contains(&(row, col)) {
            return false;
        }
        
        if index == word.len()-1 {
            return board[row][col] == word[index];
        }
        
        visited.insert((row, col));
        let neighbors = Solution::get_neighbors(board, row, col);
        
        for neighbor in neighbors {
            
            if Solution::find_word(index+1, neighbor[0], neighbor[1], board, word, visited) {
                return true;
            }
            
        }
        
        visited.remove(&(row, col));
        return false;
    }
    
    
    // O((m*n)^2) time,
    // O(m*n) space,
    // Approach: backtracking, matrix
    pub fn exist(board: Vec<Vec<char>>, word: String) -> bool {
        
        let mut str_list: Vec<char> = word.chars().collect();
        
        for row in 0..board.len() {
            for col in 0..board[0].len() {
                
                if Solution::find_word(0, row, col, &board, &str_list, &mut HashSet::new()) {
                    return true;
                } 
            }
        }
        
        return false;
    }
}