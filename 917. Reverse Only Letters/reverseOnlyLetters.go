package RevereseLetters

import "unicode"

// O(n) time,
// O(n) space,
// Approach: two pointers,
func reverseOnlyLetters(s string) string {
    // alphabets ascii 65-122
    chars := []rune(s)
    size := len(s)
    left, right := 0, size-1
    
    for left < right {
        for left < size && !unicode.IsLetter(chars[left]) {
            left++
        }
        for right >= 0 && !unicode.IsLetter(chars[right]) {
            right--
        }
        
        // swap
        if left < right {
            chars[left], chars[right] = chars[right], chars[left]
        }
        left++
        right--
    }
    
    return string(chars)
}