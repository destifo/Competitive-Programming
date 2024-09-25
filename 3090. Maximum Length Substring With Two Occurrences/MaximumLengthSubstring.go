package MaximumLengthSubstring

// O(n) time,
// O(n) space,
// Approach: two pointers, 
func maximumLengthSubstring(s string) int {
    left, right := 0, 0
    count := map[rune]int{}
    chars := []rune(s)
    maxLen := 0
    
    for right < len(s) {
        currChar := chars[right]
        count[currChar]++
        for count[currChar] > 2 {
            count[chars[left]]--
            left++
        }
        
        currLen := right-left+1
        maxLen = max(maxLen, currLen)
        
        right++
    }
    
    return maxLen
}