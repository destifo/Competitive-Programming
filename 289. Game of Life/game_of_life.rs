impl Solution {
    
    pub fn in_bounds(row: usize, col: usize, ROWS: usize, COLS: usize) -> bool{
        if row < 0 || row >= ROWS{
            return false;
        }
        
        if col < 0 || col >= COLS {
            return false;
        }
        
        return true;
    }
    
    pub fn get_alive_number(row: usize, col: usize, board: &mut Vec<Vec<i32>> ) -> i32 {
        
        let ROWS = board.len();
        let COLS = board[0].len();
        
        let mut alive = 0;
        
        let directions = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]];
        
        for direction in directions {
            let mut x = (row as i32 + direction[0]) as usize;
            let mut y = (col as i32 + direction[1])  as usize;
            
            if Solution::in_bounds(x, y, ROWS, COLS) && board[x][y] == 1{
                alive += 1;
            }
        }
        
        return alive;
        
    }
    
    
    // O(ROWS*COLS) time,
    // O(ROWS*COLS) space,
    // Approach: matrix, simulation, 
    pub fn game_of_life(board: &mut Vec<Vec<i32>>) {
                
        let ROWS = board.len();
        let COLS = board[0].len();
        
        
        let mut change: Vec<[usize; 2]> = Vec::new();
        
        for row in 0..ROWS {
            for col in 0..COLS {
                let alive = Solution::get_alive_number(row, col, board);
                
                let mut next_state = board[row][col];
                
                if alive < 2 || alive > 3 {
                    next_state = 0;
                }
                else if alive == 2 {
                    next_state = board[row][col];
                }
                else {
                    next_state = 1;
                }
                
                if next_state != board[row][col] {
                    change.push([row, col]);
                }
                
            }
        }
        
        for coordinate in change {
            let row = coordinate[0];
            let col = coordinate[1];

            board[row][col] -=1;
            board[row][col] = board[row][col].abs();
        }
        
    }  
    
}