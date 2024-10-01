package PlusOne


// O(n) time,
// O(n) space,
// Approach: simualtion, math, array
func plusOne(digits []int) []int {
    right := len(digits)-1
    
    leftOver := true
    for right >= 0 && leftOver {
        digits[right] += 1
        if digits[right] > 9 {
            leftOver = true
        } else {
            leftOver = false
        }
        right--
    }
    
    if leftOver {
        digits = append([]int{1}, digits...)
    }
    
    return digits
}