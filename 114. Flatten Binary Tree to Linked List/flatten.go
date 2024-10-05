package Flatten

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isLeaf(node *TreeNode) bool {
	return node.Left == nil && node.Right == nil
}

// returns the predecessor in the process
func flat(root *TreeNode) *TreeNode {
	if root == nil || isLeaf(root) {
		return root
	}

	var leftPred *TreeNode
	if root.Left != nil {
		leftPred = flat(root.Left)
	}

	var rightPred *TreeNode
	if root.Right != nil {
		rightPred = flat(root.Right)
	}

	// if we have a left subtree, we attach the right flattned sub tree to the left flattned, then we move left flattned to the node's right path
	if leftPred != nil {
		leftPred.Right = root.Right
		root.Right = root.Left
		root.Left = nil
	}

	// if we have right subtree, that's gonna be our predecessor
	if rightPred != nil {
		return rightPred
	}

	return leftPred
}

// O(n) time,
// O(1) space,
// Approach: tree, dfs, recursion,
func flatten(root *TreeNode) {
	// we need to know the predecessor of the right node of the current node we are at, for example node 4 for node 1's right node(which is 5)

	_ = flat(root)
}
