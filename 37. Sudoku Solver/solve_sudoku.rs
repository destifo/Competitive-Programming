use std::collections::HashSet;


fn get_sub_box(row: usize, col: usize) -> usize {
    (row / 3) * 3 + col / 3
}

fn is_last_cell(row: usize, col: usize) -> bool {
    let dimension = 9;
    row == dimension-1 && col == dimension
}

fn is_valid(
row: usize,
col: usize,
val: usize, 
row_maps: &mut Vec<Vec<bool>>,
col_maps: &mut Vec<Vec<bool>>,
sub_box_maps: &mut Vec<Vec<bool>>
) -> bool {
    !(row_maps[row][val] || col_maps[col][val] || sub_box_maps[get_sub_box(row, col)][val])
}


fn solve(
    row: usize,
    col: usize,
    board: &mut Vec<Vec<char>>, 
    row_maps: &mut Vec<Vec<bool>>,
    col_maps: &mut Vec<Vec<bool>>,
    sub_box_maps: &mut Vec<Vec<bool>>
    ) -> bool {
        let dimension = 9 as usize;
        let next_row: usize;
        let next_col: usize;

        if row >= dimension {
            return true;
        }
        
        if col + 1 == dimension {
            next_row = row + 1;
            next_col = 0;
        } else {
            next_row = row;
            next_col = col + 1;
        }

        if board[row][col] != '.' && is_last_cell(row, col) {
            return true;
        }

        if board[row][col] != '.' {
            return solve(
                next_row,
                next_col,
                board,
                row_maps,
                col_maps,
                sub_box_maps,
            );
        }

        // println!("board: {:?}", board);
        for val in 1..10_usize {
            if !is_valid(row, col, val, row_maps, col_maps, sub_box_maps) {
                continue;
            }

            if let Some(char_val) = char::from_digit(val as u32, 10) {
                board[row][col] = char_val;
            }

            if is_last_cell(row, col) {
                return true;
            }
            
            row_maps[row][val] = true;
            col_maps[col][val] = true;
            sub_box_maps[get_sub_box(row, col)][val] = true;

            if solve(next_row, next_col, board, row_maps, col_maps, sub_box_maps) {
                return true;
            }

            board[row][col] = '.';
            row_maps[row][val] = false;
            col_maps[col][val] = false;
            sub_box_maps[get_sub_box(row, col)][val] = false;
        }

        false
    }

impl Solution {
    pub fn solve_sudoku(board: &mut Vec<Vec<char>>) {

        let mut row_maps = vec![vec![false;10];9];
        let mut col_maps = vec![vec![false;10];9];
        let mut sub_box_maps = vec![vec![false;10];9];
        let dimension = 9 as usize;

        for row in 0..dimension {
            for col in 0..dimension {
                let cell = board[row][col];
                if cell  == '.' {
                    continue;
                }

                let cell = cell.to_digit(10).unwrap() as usize;
                row_maps[row][cell] = true;
                col_maps[col][cell] = true;
                sub_box_maps[get_sub_box(row, col)][cell] = true;
            }
        }

        // build board
        let _ = solve(
            0,
            0,
            board,
            &mut row_maps,
            &mut col_maps,
            &mut sub_box_maps,
        );
    }
}
