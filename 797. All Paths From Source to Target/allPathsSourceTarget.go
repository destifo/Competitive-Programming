package allPathsSourceTarget


// O(n+e) time,
// O(n) space,
// Approach: dfs, backtracking, 
func traverse(node int, path *[]int, graph *[][]int, pathes *[][]int) {
    *path = append(*path, node)
    if node == len(*graph)-1 {
        final_path := make([]int, len(*path))
        copy(final_path, *path)
        (*pathes) = append(*pathes, final_path)
        *path = (*path)[:len(*path)-1]
        return
    }
    
    for _, nbr := range (*graph)[node] {
        traverse(nbr, path, graph, pathes)
    }
    *path = (*path)[:len(*path)-1]
}


func allPathsSourceTarget(graph [][]int) [][]int {
    var all_pathes [][]int
    var path []int
    traverse(0, &path, &graph, &all_pathes)
    
    return all_pathes
}