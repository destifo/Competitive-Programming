package uniquePathsIII


func inBounds(row int, col int, ROWS int, COLS int) bool {
    if row < 0 || row >= ROWS || col < 0 || col >= COLS {
        return false
    }
    return true
}


func getNeighbors(row int, col int, grid *[][]int) [][]int {
    var nbrs [][]int
    
    directions := [][]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
    for _, coord := range directions {
        x := coord[0]
        y := coord[1]
        if inBounds(row+x, col+y, len(*grid), len((*grid)[0])) && (*grid)[row+x][col+y] != -1 {
            nbrs = append(nbrs, []int{row+x, col+y})
        }
    }
    
    return nbrs
}


func findUniquePaths(row int, col int, grid *[][]int, obstacles int) int {
    if (*grid)[row][col] == 2 {
        if len(*grid) * len((*grid)[0]) -1 == obstacles {
            return 1
        }
        return 0
    }
    
    (*grid)[row][col] = -1
    
    paths := 0
    for _, coord := range getNeighbors(row, col, grid){
        paths += findUniquePaths(coord[0], coord[1], grid, obstacles+1)
    }
    (*grid)[row][col] = 0
    
    return paths
}


// O((log(4))^m*n) time, 
// O(m*n) space, 
// Approach: backtracking, 
func uniquePathsIII(grid [][]int) int {
    paths := 0
    obstacles := 0
    start_row := 0
    start_col := 0
    ROWS := len(grid)
    COLS := len(grid[0])
    
    for row := 0; row < ROWS; row++ {
        for col := 0; col < COLS; col++ {
            if grid[row][col] == -1 {
                obstacles += 1
            } else if grid[row][col] == 1 {
                start_row = row
                start_col = col
            }
        }
    }
    
    paths += findUniquePaths(start_row, start_col, &grid, obstacles)
    return paths
}