
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    
    def buildNewGraph(self, node: 'Node', node_memo: dict['Node']) -> 'Node':
        if not node:
            return node
        
        if node.val in node_memo:
            return node_memo[node.val]
        
        new_node = Node(node.val)
        node_memo[node.val] = new_node
        for nbr in node.neighbors:
            new_node.neighbors.append(self.buildNewGraph(nbr, node_memo))
            
        return new_node
    
    
    # O(n) time,
    # O(n) space,
    # Approach: recursion, graph, linked list
    def cloneGraph(self, node: 'Node') -> 'Node':
        node_dictionary = {}
        return self.buildNewGraph(node, node_dictionary)