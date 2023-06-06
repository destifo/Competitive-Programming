package detectCapitalUse


import "strings"


// O(n) time,
// O(n) space,
// Approach: string manipulation,
func detectCapitalUse(word string) bool {
    upper := strings.ToUpper(word)
    lower := strings.ToLower(word)
    
    if word == upper || word == lower {
        return true
    }
    
    chars := []rune(word)
    for i, char := range chars {
        if i == 0 {
            continue
        }
        char_str := string(char)
        upper_char := strings.ToUpper(char_str)
        if upper_char == char_str {
            return false
        }
    }
    return true
}