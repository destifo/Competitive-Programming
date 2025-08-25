impl Solution {

    // O(n*m) time,
    // O(n*m) space,
    // Approach: simulation, matrix
    pub fn find_diagonal_order(mat: Vec<Vec<i32>>) -> Vec<i32> {
        let mut move_up_right = true;
        let (mut x, mut y) = (0, 0);
        let mut ans = vec![];
        let (rows, cols) = (mat.len() as i32, mat[0].len() as i32);

        let final_size = rows * cols;

        while ans.len() != final_size as usize {
            ans.push(mat[x as usize][y as usize]);
            match move_up_right {
                true => {
                    x -= 1;
                    y += 1;
                },
                false => {
                    x += 1;
                    y -= 1;
                }
            }

            if x == -1 || y == cols {
                // diagonal up-right ended
                if y < cols {
                    x += 1;
                } else {
                    x += 2;
                    y -= 1;
                }
                move_up_right = false;
            }

            if x == rows || y == -1 {
                // diagonal bottom left ended
                if x < rows {
                    y += 1;
                } else {
                    x -= 1;
                    y += 2;
                }
                move_up_right = true;
            }
        }

        ans
    }
}
