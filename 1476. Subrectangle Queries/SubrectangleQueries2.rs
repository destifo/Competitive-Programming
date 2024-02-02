struct SubrectangleQueries {
    pub matrix: Vec<Vec<i32>>,
    pub updates: Vec<Vec<i32>>
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl SubrectangleQueries {

    fn new(rectangle: Vec<Vec<i32>>) -> Self {
        Self {
            matrix: rectangle,
            updates: vec![]
        }
    }
    
    fn update_subrectangle(&mut self, row1: i32, col1: i32, row2: i32, col2: i32, new_value: i32) {
        self.updates.push(vec![row1, row2, col1, col2, new_value]);
    }
    
    fn get_value(&self, row: i32, col: i32) -> i32 {
        for i in (0..self.updates.len()).rev() {
            if row >= self.updates[i][0] && row <= self.updates[i][1] && col >= self.updates[i][2] && col <= self.updates[i][3] {
                return self.updates[i][4];
            }
        }
        
        self.matrix[row as usize][col as usize]
    }
}

/**
 * Your SubrectangleQueries object will be instantiated and called as such:
 * let obj = SubrectangleQueries::new(rectangle);
 * obj.update_subrectangle(row1, col1, row2, col2, newValue);
 * let ret_2: i32 = obj.get_value(row, col);
 */