/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Children []*Node
 * }
 */

 func traverse(node *Node, answer *[]int) {
    if node == nil {
        return;
    }
    
    for _, child := range node.Children {
        traverse(child, answer);
    }
    
    *answer = append(*answer, node.Val);
}


// O(n) time,
// O(n) space,
// Approach: dfs, recursion, tree
func postorder(root *Node) []int {
    var answer []int;
    traverse(root, &answer);
    
    return answer;
}