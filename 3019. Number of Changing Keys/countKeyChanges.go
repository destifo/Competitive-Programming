package CountKeyChanges

import "strings"

// O(n) time,
// O(n) space,
// Approach: counting, 
func countKeyChanges(s string) int {
    size := len(s)
    chars := []rune(s)
    
    changes := 0
    for i := 1; i < size; i++ {
        if strings.ToLower(string(chars[i])) != strings.ToLower(string(chars[i-1])) {
            changes++
        }
    } 
    
    return changes
}