fn inbound(row: i32, col: i32, board: &mut Vec<Vec<char>>) -> bool {
    let (ROWS, COLS) = (board.len() as i32, board.first().unwrap().len() as i32);

    if row < 0 || row >= ROWS {
        return false;
    }

    if col < 0 || col >= COLS {
        return false;
    }

    true
}

fn get_neighbors(coord: (usize, usize), board: &mut Vec<Vec<char>>) -> Vec<(usize, usize)> {
    let (row, col) = coord;
    let mut nbrs = vec![];

    let directions = [(0, 1), (0, -1), (1, 0), (-1, 0)];

    for (x, y) in directions {
        let (new_row, new_col) = (row as i32 + x, col as i32 + y);

        if inbound(new_row, new_col, board) {
            nbrs.push((new_row as usize, new_col as usize));
        }
    }

    nbrs
}

fn is_possible(
    index: usize,
    curr: (usize, usize),
    board: &mut Vec<Vec<char>>,
    chars: &Vec<char>,
) -> bool {
    if index == chars.len() {
        return true;
    }

    let (row, col) = curr;
    let curr_char = board[row][col];
    board[row][col] = '*';

    for (nbr_row, nbr_col) in get_neighbors(curr, board) {
        if board[nbr_row][nbr_col] == chars[index]
            && is_possible(index + 1, (nbr_row, nbr_col), board, chars)
        {
            return true;
        }
    }

    board[row][col] = curr_char;
    false
}

impl Solution {
    // O((n*m)^2) time,
    // O(n*m) space,
    // Approach: dfs,
    pub fn exist(mut board: Vec<Vec<char>>, word: String) -> bool {
        let (ROWS, COLS) = (board.len(), board.first().unwrap().len());
        let chars: Vec<char> = word.chars().collect();

        for row in 0..ROWS {
            for col in 0..COLS {
                if board[row][col] == chars[0] && is_possible(1, (row, col), &mut board, &chars) {
                    return true;
                }
            }
        }

        false
    }
}
