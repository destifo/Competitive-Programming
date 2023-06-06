

import "math";


// Definition for a binary tree node.
type TreeNode struct {
    Val int
    Left *TreeNode
    Right *TreeNode
}


 // O(n) time,
 // O(n) space, for the call stack,
 // Approach: dfs, tree, 
 func goZigzag(node *TreeNode, max_val *float64) (float64, float64) {
	 if node == nil {
		 return -1.0, -1.0;
	 }
	 
	 _, val1 := goZigzag(node.Left, max_val);
	 go_left := val1 + 1.0;
	 val2, _ := goZigzag(node.Right, max_val);
	 go_right := val2 + 1.0;
	 *max_val = math.Max(*max_val, math.Max(go_left, go_right));
	 
	 return go_left, go_right;
 }
 
 
 func longestZigZag(root *TreeNode) int {
	 max_val := float64(0);
	 goZigzag(root, &max_val);
	 
	 return int(max_val);
 }