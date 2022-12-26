package canReach


func inBounds(x int, length int) bool {
    return !(x < 0 || x >= length)
}


func isReachable(index int, nums *[]int) bool {
    
    val := (*nums)[index]
    if val == 0 {
        return true
    }
    
    if val == -1 {
        return false
    }
    
    (*nums)[index] = -1;
    if inBounds(index-val, len(*nums)) && isReachable(index-val, nums) {
        return true
    } else if inBounds(index+val, len(*nums)) && isReachable(index+val, nums) {
        return true
    }
    
    return false
}


// O(n) time,
// O(1) space,
// Approach: dfs, 
func canReach(arr []int, start int) bool {    
    return isReachable(start, &arr)
}