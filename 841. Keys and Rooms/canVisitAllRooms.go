// O(n) time,
// O(n) space,
// Approach: dfs, stack, hashmap
func canVisitAllRooms(rooms [][]int) bool {
    visited := make(map[int]bool);
    stack := make([]int, 0);
    stack = append(stack, 0);
    visited[0] = true;
    
    for len(stack) > 0 {
        room := stack[len(stack)-1];
        stack = stack[:len(stack)-1];
        
        for _, key := range rooms[room] {
            _, ok := visited[key];
            if ok {
                continue;
            }
            
            visited[key] = true;
            stack = append(stack, key);
        }
    }
    
    return len(visited) == len(rooms);
}


// O(n) time,
// O(n) space,
// Approach: bfs, queue, hashmap
func canVisitAllRooms2(rooms [][]int) bool {
    visited := make(map[int]bool);
    queue := make([]int, 0);
    queue = append(queue, 0);
    visited[0] = true;
    
    for len(queue) > 0 {
        queue_len := len(queue);
        for i := 0; i < queue_len; i++ {
            room := queue[0];
            queue = queue[1:];
            
            for _, key := range rooms[room] {
                _, exists := visited[key];
                if exists {
                    continue;
                }
                visited[key] = true;
                queue = append(queue, key);
            }
        } 
    }
    
    return len(visited) == len(rooms);
}