use std::collections::HashSet;


impl Solution {
    
    fn in_bounds(row: i32, col: i32) -> bool {
        return !(row < 0 || row > 8 || col < 0 || col > 8);
    }
    
    
    fn move_piece(row: i32, col: i32, direction: (i32, i32), queens: &HashSet<(i32, i32)>) -> Vec<i32> {
        
        if queens.contains(&(row, col)) {
            return vec![row, col];
        }
        
        if !Solution::in_bounds(row, col) {
            return vec![-1, -1];
        }
        
        return Solution::move_piece(row+direction.0, col+direction.1, direction, queens);
    }
    
    
    pub fn queens_attackthe_king(queens: Vec<Vec<i32>>, king: Vec<i32>) -> Vec<Vec<i32>> {
        let directions = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, -1], [1, 1], [-1, -1], [-1, 1]];
        let mut answer = Vec::new();
        let mut queens_set: HashSet<(i32, i32)> = HashSet::new();
        for queen in queens {
            queens_set.insert((queen[0], queen[1]));
        }
        
        for direction in directions {
            let queen = Solution::move_piece(king[0], king[1], (direction[0], direction[1]), &queens_set);
            if queen[0] != -1 {
                answer.push(queen);
            }
        }
        return answer;
    }
}