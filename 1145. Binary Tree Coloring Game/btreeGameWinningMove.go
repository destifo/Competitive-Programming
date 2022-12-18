/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

 import "fmt";

 func findNode(val int, root *TreeNode) *TreeNode {
	 
	 var stack []*TreeNode;
	 stack = append(stack, root);
	 
	 for len(stack) > 0 {
		 node := stack[0];
		 stack = stack[1:];
		 if node.Val == val {
			 return node;
		 }
		 if node.Left != nil {
			 stack = append(stack, node.Left);
		 }
		 if node.Right != nil {
			 stack = append(stack, node.Right);
		 }
	 }
	 
	 return nil;
 }
 
 
 func countNodes(root *TreeNode) int {
	 if root == nil {
		 return 0;
	 }
	 return countNodes(root.Left) + countNodes(root.Right) + 1;
 }
 
 
 // O(n) time,
 // O(n) space, n for the recursive call stack, cld be skewed(linkedlist) tree
 // Approach: dfs, tree, 
 func btreeGameWinningMove(root *TreeNode, n int, x int) bool {
	 node := findNode(x, root);
	 
	 total_nodes := countNodes(root);
	 left_subtree_nodes := countNodes(node.Left);
	 right_subtree_nodes := countNodes(node.Right);
	 node_childs := left_subtree_nodes+right_subtree_nodes;
	 upper_subtree_nodes := total_nodes - (node_childs+1);
	 if upper_subtree_nodes > node_childs+1 {
		 return true;
	 }
	 if right_subtree_nodes > total_nodes-right_subtree_nodes {
		 return true;
	 }
	 if left_subtree_nodes > total_nodes-left_subtree_nodes {
		 return true;
	 }
	 return false;
 }