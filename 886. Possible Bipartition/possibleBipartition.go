package possibleBipartition;


func colorGraph(node int, color int, graph *[][]int, colors *[]int) bool {
    
    (*colors)[node] = color;
    if color == 1 {
        color = 2;
    } else {
        color = 1;
    }
    for _, dislike := range (*graph)[node] {
        if (*colors)[node] == (*colors)[dislike] {
            return false;
        }
        if (*colors)[dislike] == 0 {
            if !colorGraph(dislike, color, graph, colors) {
                return false;
            }
        }
    }
    
    return true;
}


// O(n + e) time, n --> nodes, e --> edges
// O(n + e) space,
// Approach: graph coloring, dfs, graph
func possibleBipartition(n int, dislikes [][]int) bool {
    colors := make([]int, n, n);
    
    graph := make([][]int, n, n);
    for _, dislike := range dislikes {
        graph[dislike[0]-1] = append(graph[dislike[0]-1], dislike[1]-1);
        graph[dislike[1]-1] = append(graph[dislike[1]-1], dislike[0]-1);
    }
    
    for i:= 0; i < n; i++ {
        if colors[i] != 0 {
            continue;
        }
        if !colorGraph(i, 1, &graph, &colors) {
            return false;
        }
    }
    
    return true;
}

func find(x int, parent *[]int) int {
    if (*parent)[x] != x {
        (*parent)[x] = find((*parent)[x], parent);
    }
    
    return (*parent)[x];
}


func union(x int, y int, parent *[]int, size *[]int) {
    x_parent := find(x, parent);
    y_parent := find(y, parent);
    
    if x_parent == y_parent {
        return;
    }
    
    if (*size)[x_parent] > (*size)[y_parent] {
        (*size)[x_parent] += (*size)[y_parent];
        (*parent)[y_parent] = x_parent;
    } else {
        (*size)[y_parent] += (*size)[x_parent];
        (*parent)[x_parent] = y_parent;
    }
}


// O(n + e) time, n --> nodes, e --> edges,
// O(n + e) space,
// Approach: union find, dfs, graph
func possibleBipartition2(n int, dislikes [][]int) bool {
    parent := make([]int, n);
    size := make([]int, n);
    for i := 0; i < n; i++ {
        parent[i] = i;
    }
    
    graph := make([][]int, n);
    for _, dislike := range dislikes {
        graph[dislike[0]-1] = append(graph[dislike[0]-1], dislike[1]-1);
        graph[dislike[1]-1] = append(graph[dislike[1]-1], dislike[0]-1);
    }
    
    for i := 0; i < n; i++ {
        first_nbr := -1
        for _, nbr := range graph[i] {
            if first_nbr == -1 {
                first_nbr = nbr;
            }
            
            if find(i, &parent) == find(nbr, &parent) {
                return false;
            }
            union(first_nbr, nbr, &parent, &size);
        }
    }
    return true;
}