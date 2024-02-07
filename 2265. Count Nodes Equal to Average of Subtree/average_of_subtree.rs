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


fn count_nodes(node: Rc<RefCell<TreeNode>>, count: &mut i32) -> (i32, i32) {
    let curr = node.borrow();
    let (mut subtree_tot, mut subtree_count) = (curr.val, 1);
    
    if let Some(left) = curr.left.as_ref() {
        let (left_tot, left_count) = count_nodes(left.clone(), count);
        subtree_tot += left_tot;
        subtree_count += left_count;
    }
    
    if let Some(right) = curr.right.as_ref() {
        let (right_tot, right_count) = count_nodes(right.clone(), count);
        subtree_tot += right_tot;
        subtree_count += right_count;
    }
    
    let subtree_avg = subtree_tot/subtree_count;
    if subtree_avg == curr.val {
        *count += 1;
    }
    
    return (subtree_tot, subtree_count);
}

use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    
    // O(n) time, n -> number of nodes
    // O(h) space, h -> height of the tree,
    // Approach: dfs, tree
    pub fn average_of_subtree(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut ans = 0;
        if let Some(node) = root {
            count_nodes(node, &mut ans);
        }
        
        ans
    }
}