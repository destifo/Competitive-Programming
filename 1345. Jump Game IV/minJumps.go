package minJumps


func minJumps(arr []int) int {
    
    indices := make(map[int][]int)
    for i, val := range arr {
        indices[val] = append(indices[val], i)
    }
    
    depth := 0;
    queue := make([]int, 0, len(arr))
    queue = append(queue, 0)
    visited := make(map[int]bool)
    visited[0] = true
    
    for len(queue) > 0 {
        queue_len := len(queue)
        for i := 0; i < queue_len; i++ {
            index := queue[0]
            queue = queue[1:]
            
            if index == len(arr)-1 {
                return depth
            }
            
            for _, nbr := range indices[arr[index]] {
                if _, found := visited[nbr]; found || nbr == index {
                    continue
                }
                visited[nbr] = true
                queue = append(queue, nbr)
            }
            delete(indices, arr[index])
            if index+1 < len(arr) {
                if _, found := visited[index+1]; !found {
                    visited[index+1] = true
                    queue = append(queue, index+1)
                }
            }
            if (index-1) >= 0 {
                if _, found := visited[index-1]; !found {
                    visited[index-1] = true
                    queue = append(queue, index-1)
                }
            }
        }
        depth += 1
    }
    
    return -1
}