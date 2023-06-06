/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

 import "math";


 // O(n) time,
 // O(n) space, a
 // Approach: bfs, 
 func largestValues(root *TreeNode) []int {
	 var answer []int;
	 var queue []*TreeNode;
	 
	 if root != nil {
		 queue = append(queue, root);
	 }
	 
	 for len(queue) > 0 {
		 n := len(queue);
		 max_val := float64(math.MinInt64);
		 for i := 0; i < n; i++ {
			 node := queue[0];
			 queue = queue[1:];
			 max_val = math.Max(max_val, float64(node.Val));
			 if node.Left != nil {
				 queue = append(queue, node.Left);
			 }
			 if node.Right != nil {
				 queue = append(queue, node.Right);
			 }
		 }
		 answer = append(answer, int(max_val));
	 }
	 
	 return answer;
 }