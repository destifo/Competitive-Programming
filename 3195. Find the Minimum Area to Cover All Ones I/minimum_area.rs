impl Solution {

    // O(n*m) time, n -> rows, m -> columns
    // O(1) space,
    // Approach: matrix, 
    pub fn minimum_area(grid: Vec<Vec<i32>>) -> i32 {
        let (mut left_end, mut right_end): (Option<usize>, Option<usize>) = (None, None);
        let (mut upper, mut lower): (Option<usize>, Option<usize>) = (None, None);

        for i in 0..grid.len() {
            for j in 0..grid[i].len() {
                if grid[i][j] == 1 {
                    // upper side
                    if upper.is_none() {
                        upper = Some(i);
                    }

                    // left side
                    match left_end {
                        None => left_end = Some(j),
                        Some(val) => {
                            if val > j {
                                left_end = Some(j)
                            }
                        }
                    }

                    // right side
                    match right_end {
                        None => right_end = Some(j+1),
                        Some(val) => {
                            if j+1 > val {
                                right_end = Some(j+1);
                            }
                        }

                    }

                    // lower side
                    lower = Some(i+1);
                }
            }
        }

        let length = right_end.unwrap() - left_end.unwrap();
        let width = lower.unwrap() - upper.unwrap();
        
        (length * width) as i32
    }
}
