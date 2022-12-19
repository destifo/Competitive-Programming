// O(n) time,
// O(n) space,
// Approach: dfs, stack,

func find(node int, parent *[]int) int {
    if node != (*parent)[node] {
        (*parent)[node] = find((*parent)[node], parent);
    }
    
    return (*parent)[node];
}


func union(node1 int, node2 int, parent *[]int, size *[]int) {
    
    parent1 := find(node1, parent);
    parent2 := find(node2, parent);
    if (*size)[parent1] > (*size)[parent2] {
        (*size)[parent1] += (*size)[parent2];
        (*parent)[parent2] = parent1;
    } else {
        (*size)[parent2] += (*size)[parent1];
        (*parent)[parent1] = parent2;
    }
}


func validPath(n int, edges [][]int, source int, destination int) bool {
    
    parent := make([]int, n);
    for i := 0; i < n; i++ {
        parent[i] = i;
    } 
    size := make([]int, n);
    
    for _, edge := range edges {
        node1 := edge[0];
        node2 := edge[1];
        union(node1, node2, &parent, &size);
    }
    return find(source, &parent) == find(destination, &parent);
}