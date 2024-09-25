package FinalString

import "slices"

// O(n^2) time,
// O(n) space,
// Approach: simulation, 
func finalString(s string) string {
    var output []rune
    chars := []rune(s)
    size, i := len(s), 0
    
    for i < size {
        revCount := 0
        if chars[i] == 'i' {
            for i < size && chars[i] == 'i' {
                i++
                revCount++
            }
        } else {
            output = append(output, chars[i])
            i++
        }
        
        if revCount % 2 == 1 {
            slices.Reverse(output)
        }
    }
    
    return string(output)
}