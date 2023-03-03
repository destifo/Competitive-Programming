from typing import List


class Node:
    
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.left = None
        self.right = None


class Solution:
    
    def isValid(self, parent, parent_child, child):
        if not child:
            return True
        
        if parent_child and parent_child != child:
            return False
            
        if child.parent and child.parent != parent:
            return False
        
        if parent == child.left or parent == child.right:
            return False
        
        return True
    
    
    def find(self, node, parent):
        
        if node != parent[node]:
            parent[node] = self.find(parent[node], parent)
            
        return parent[node]
    
    
    def union(self, node1, node2, parent):
        
        parent1 = self.find(node1, parent)
        parent2 = self.find(node2, parent)
        
        if parent1 < parent2:
            parent[parent2] = parent1
        else:
            parent[parent1] = parent2
    
    
    # O(n) time,
    # O(n) space,
    # Approach: tree, graph, union find
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        nodes = {}
        nodes[-1] = None
        parent = [i for i in range(n)]
        
        for i in range(n):
            if i not in nodes:
                nodes[i] = Node(i)
            curr_node = nodes[i]
            
            if leftChild[i] not in nodes:
                nodes[leftChild[i]] = Node(leftChild[i])
            left_child_node = nodes[leftChild[i]]
                
            if not self.isValid(curr_node, curr_node.left, left_child_node):
                return False
            
            if left_child_node:
                left_child_node.parent = curr_node
                curr_node.left = left_child_node
                if self.find(curr_node.val, parent) == self.find(left_child_node.val, parent):
                    return False
                self.union(curr_node.val, left_child_node.val, parent)
            
            if rightChild[i] not in nodes:
                nodes[rightChild[i]] = Node(rightChild[i])
                
            right_child_node = nodes[rightChild[i]]
            if not self.isValid(curr_node, curr_node.right, right_child_node):
                return False
            
            if right_child_node:
                right_child_node.parent = curr_node
                curr_node.right = right_child_node
                if self.find(curr_node.val, parent) == self.find(right_child_node.val, parent):
                    return False
                self.union(curr_node.val, right_child_node.val, parent)
            
        for i in range(n):
            if self.find(i, parent) != 0:
                return False
            
        return True