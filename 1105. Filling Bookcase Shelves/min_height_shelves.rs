use std::collections::HashMap;
use std::cmp;

impl Solution {
    
    
    pub fn find_ordering(index: usize, books: &Vec<Vec<i32>>, curr_width: i32, max_height: i32, width_limit: i32, memo: &mut HashMap<(usize, i32), i32>) -> i32 {
        
        if index >= books.len() {
            return max_height;
        }
        
        if memo.contains_key(&(index, curr_width)) {
            return *memo.get(&(index, curr_width)).unwrap_or(&0);
        }
        
        let book = &books[index];
        let book_width = book[0];
        let book_height = book[1];
        
        let mut same_row = i32::MAX;
        let mut skip_row = i32::MAX;
        
        if curr_width + book_width <= width_limit {
            same_row = Solution::find_ordering(index+1, books, curr_width + book_width, cmp::max(max_height, book_height), width_limit, memo);
        }
        
        if index != 0 {
            skip_row = max_height + Solution::find_ordering(index+1, books, book_width, book_height, width_limit, memo);
        }
        
        memo.insert((index, curr_width), cmp::min(same_row, skip_row));
        return *memo.get(&(index, curr_width)).unwrap_or(&0);
    }
    
    
    // O(n*sum(books_width)) time,
    // O(n*sum(books_width)) space,
    // Approach: dp, memoization
    pub fn min_height_shelves(books: Vec<Vec<i32>>, shelf_width: i32) -> i32 {
        let mut memo = HashMap::new();
        return Solution::find_ordering(0, &books, 0, 0, shelf_width, &mut memo);
    }
}