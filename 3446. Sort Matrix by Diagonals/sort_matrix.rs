
fn out_of_bounds(row: usize, col: usize, grid: &Vec<Vec<i32>>) -> bool {
    row >= grid.len() || col >= grid[0].len()
}


fn move_bottom_right(row: usize, col: usize) -> (usize, usize) {
    (row + 1, col + 1)
}

impl Solution {

    // O(n^1logn^2) time
    // O(n) space, n coz using rust but n^2 in total
    // Approach: sorting, 
    pub fn sort_matrix(grid: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut grid = grid;

        for i in (0..grid.len()).rev() {
            let mut diagonal = vec![];
            let (mut curr_row, mut curr_col) = (i, 0 as usize);

            while !out_of_bounds(curr_row, curr_col, &grid) {
                diagonal.push(grid[curr_row][curr_col]);
                (curr_row, curr_col) = move_bottom_right(curr_row, curr_col);
            }

            diagonal.sort_by(|a, b| b.cmp(a));
            (curr_row, curr_col) = (i, 0 as usize);
            println!("{:?}", diagonal);
            for num in diagonal {
                grid[curr_row][curr_col] = num;
                (curr_row, curr_col) = move_bottom_right(curr_row, curr_col);
            }

        }

        for j in 1..grid[0].len() {
            let mut diagonal = vec![];
            let (mut curr_row, mut curr_col) = (0 as usize, j);

            while !out_of_bounds(curr_row, curr_col, &grid) {
                diagonal.push(grid[curr_row][curr_col]);
                (curr_row, curr_col) = move_bottom_right(curr_row, curr_col);
            }

            diagonal.sort();
            (curr_row, curr_col) = (0 as usize, j);
            for num in diagonal {
                grid[curr_row][curr_col] = num;
                (curr_row, curr_col) = move_bottom_right(curr_row, curr_col);
            }
        }

        grid
    }
}
