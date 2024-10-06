package FlattenMultilevelDoublyLinkedList

type Node struct {
	Val   int
	Prev  *Node
	Next  *Node
	Child *Node
}

func flat(root *Node) *Node {
	if root == nil {
		return root
	}

	if root.Child != nil {
		rightNode := root.Next
		child := root.Child

		// remove child link
		root.Child = nil

		// restructure
		middleEnd := flat(child)
		child.Prev = root
		root.Next = child
		middleEnd.Next = rightNode
		if rightNode != nil {
			rightNode.Prev = middleEnd
		}
		root = middleEnd
	}

	rightEnd := flat(root.Next)
	if rightEnd != nil {
		return rightEnd
	}

	return root
}

// O(n) time, one pass -- n => no of nodes,
// O(1) space,
// Approach: recursion, linked list
func flatten(root *Node) *Node {
	_ = flat(root)

	return root
}
