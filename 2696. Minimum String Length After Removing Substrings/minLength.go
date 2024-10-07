package MinLengthAfterRemove

func remove(s string) string {
    
    toBeRemoved := map[int]bool{}
    for i := 0; i < len(s)-1; i++ {
        currPair := s[i:i+2]
        if currPair == "AB" || currPair == "CD" {
            toBeRemoved[i] = true
            toBeRemoved[i+1] = true
        }
    }
    
    var afterRemoveStr string
    for i := 0; i < len(s); i++ {
        if toBeRemoved[i] {
            continue
        }
        afterRemoveStr += string(s[i])
    }
    
    return afterRemoveStr
}


// O(n^2) time,
// O(n^2) space,
// Approach: simulation, 
func minLength(s string) int {
    curr := ""
    
    for s != curr {
        curr = s
        s = remove(s)
    }
    
    return len(s)
}