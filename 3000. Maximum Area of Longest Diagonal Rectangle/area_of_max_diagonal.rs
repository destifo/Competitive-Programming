impl Solution {

    // O(n) time,
    // O(1) space,
    // Approach: iteration, 
    pub fn area_of_max_diagonal(dimensions: Vec<Vec<i32>>) -> i32 {
        let mut max_diagonal_square = 0;
        let mut max_area = 0;

        for dimension in dimensions {
            let (length, width) = (dimension[0], dimension[1]);
            let diagonal_square = length.pow(2) + width.pow(2);
            let area = length * width;

            if (diagonal_square > max_diagonal_square) ||
                (diagonal_square == max_diagonal_square && area > max_area) {
                max_diagonal_square = diagonal_square;
                max_area = area;
            }
        }

        max_area
    }
}
