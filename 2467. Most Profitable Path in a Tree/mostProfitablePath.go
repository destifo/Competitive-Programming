package MostProfitablePath

import "math"

// downward graph,
func isLeaf(node int, graph map[int][]int) bool {
    return len(graph[node]) == 0
}


// if both alice and bob reach a node at the same time, we take half,
// if alice reaches a node before bob, or bob doesn't reach it all, we take all the amount
// if bob gets there before alice, then we take nothing
func getAlicesIncome(bobsTime int, alicesTime int, amount int) int {
    income := 0
    if alicesTime == bobsTime {
        income += amount/2
    } else if alicesTime < bobsTime || bobsTime == 0 {
        income += amount
    }
    
    return income
}


func findMaxIncome(curr int, graph map[int][]int, time int, bobsTimeAtNode map[int]int, amount []int) int {
    currAmount := amount[curr]
    bobTime := bobsTimeAtNode[curr]
    
    // we can get alices's income from a node based on the time of alice at that node, and bob's time at that node
    currIncome := getAlicesIncome(bobTime, time, currAmount)
    if isLeaf(curr, graph) {
        return currIncome
    }
    
    bestPath := math.MinInt32
    for _, nbr := range graph[curr] {
        pathIncome := findMaxIncome(nbr, graph, time+1, bobsTimeAtNode, amount)
        bestPath = int(math.Max(float64(bestPath), float64(pathIncome)))
    }
    
    return bestPath + currIncome
}


// O(n) time, 3n actaully
// O(n) space,
// Approach: graph, dfs, bfs
func mostProfitablePath(edges [][]int, bob int, amount []int) int {
    
    // build the undirected graph
    graph := map[int][]int{}
    for _, edge := range edges {
        a, b := edge[0], edge[1]
        graph[a] = append(graph[a], b)
        graph[b] = append(graph[b], a)
    }
    
    // build the tree, upwards and downwards
    // downwards for alices's traversal
    // upwards for bob's traversal
    visited := map[int]bool{}
    downwardGraph := map[int][]int{}
    upwardGraph := map[int]int{}
    queue := []int{0}
    
    for len(queue) != 0 {
        queueLen := len(queue)
        for i := 0; i < queueLen; i++ {
            node := queue[0]
            queue = queue[1:]
            visited[node] = true
            
            for _, nbr := range graph[node] {
                if _, exists := visited[nbr]; !exists {
                    queue = append(queue, nbr)
                    downwardGraph[node] = append(downwardGraph[node], nbr)
                    upwardGraph[nbr] = node
                }
            }
        }
    }
    
    // we calculate bob's time at each node to his path to the root node,
    // notice here that bob has only one path to the root, so it's easy to calculate when he will be at each node in his path
    bobsTimeAtNode := map[int]int{}
    time := 0
    for bob != 0 {
        time++
        bobsTimeAtNode[bob] = time
        bob = upwardGraph[bob]
    }
    
    // we find the max income for alice, now that we have bob's time at nodes in his path
    return findMaxIncome(0, downwardGraph, 1, bobsTimeAtNode, amount)
}