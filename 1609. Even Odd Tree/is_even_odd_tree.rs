// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
// 
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::rc::Rc;
use std::cell::RefCell;
use std::collections::{VecDeque};



fn is_valid_level(level: i32, nums: &Vec<i32>) -> bool {
    match level % 2 {
        0 => {
            let mut prev_num = 0;
            for num in nums {
                if *num <= prev_num || *num % 2 == 0 {
                    return false;
                }
                prev_num = *num;
            }
            return true;
        },
        _ => {
            let mut prev_num = i32::MAX;
            for num in nums {
                if *num >= prev_num || *num % 2 == 1 {
                    return false;
                }
                prev_num = *num;
            }
            return true;
        }
    }
}


impl Solution {
    
    // O(n) time, n -> no of nodes
    // O(n) space,
    // Approach: bfs, 
    pub fn is_even_odd_tree(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        let mut queue: VecDeque<Rc<RefCell<TreeNode>>> = VecDeque::new();
        if let Some(node) = root {
            queue.push_back(node);
        }
        
        let mut level = 0;
        while !queue.is_empty() {
            let queue_len = queue.len();
            let mut level_arr = vec![];
            for _ in 0..queue_len {
                let node = queue.pop_front().unwrap();
                let node = node.borrow();
                level_arr.push(node.val.clone());
                if let Some(left_node) = node.left.clone() {
                    queue.push_back(left_node);
                }
                if let Some(right_node) = node.right.clone() {
                    queue.push_back(right_node);
                }
            }
            if !is_valid_level(level, &level_arr) {
                return false;
            }
            level_arr = vec![];
            level += 1;
        }
        
        true
    }
}