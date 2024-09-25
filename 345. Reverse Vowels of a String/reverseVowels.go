package ReverseVowels


import "strings"

// O(n) time, n -> len(s)
// O(n) space,
// Approach: two pointers, 
func reverseVowels(s string) string {
    vowels := map[string]bool{
        "a": true,
        "e": true,
        "i": true,
        "o": true,
        "u": true,
    }
    
    chars := []rune(s)
    size := len(s)
    
    left, right := 0, size-1
    
    for left < right {
        
        // move right
        for left < size && !vowels[strings.ToLower(string(chars[left]))] {
            left++
        }
        
        // move left
        for right >= 0 && !vowels[strings.ToLower(string(chars[right]))] {
            right--
        }
        
        if left < right {
            // swap
            chars[left], chars[right] = chars[right], chars[left]
        }
        left++
        right--
    }
    
    return string(chars)
}