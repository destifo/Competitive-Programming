package MakeSmallestPalindrome


// O(n) time,
// O(n) space,
// Approach: two pointers, 
func makeSmallestPalindrome(s string) string {
    chars := []rune(s)
    left, right := 0, len(s)-1
    
    for left < right {
        if chars[left] == chars[right] {
            left++
            right--
            continue
        }
        
        minChar := chars[left]
        if int(chars[right]) < int(chars[left]) {
            minChar = chars[right]
        }
        chars[left], chars[right] = minChar, minChar
        left++
        right--
    }
    
    return string(chars)
}