package AddStrings


import (
	"strconv"
	"slices"
)


// O(n) time,
// O(n) space,
// Approach: simulation, 
func addStrings(num1 string, num2 string) string {
    digits1, digits2 := []rune(num1), []rune(num2)
    
    p1, p2 := len(num1)-1, len(num2)-1
    res := []rune{}
    
    leftOver := 0
    for p1 >= 0 && p2 >= 0 {
        digit1, _ := strconv.Atoi(string(digits1[p1]))
        digit2, _ := strconv.Atoi(string(digits2[p2]))
        
        sum := digit1 + digit2 + leftOver
        if sum > 9 {
            leftOver = 1
        } else {
            leftOver = 0
        }
        
        s := strconv.Itoa(sum%10)
        val := []rune(s)
        res = append(res, val...)
        p1--
        p2--
    }
    
    for p1 >= 0 {
        digit1, _ := strconv.Atoi(string(digits1[p1]))
        sum := digit1 + leftOver
        if sum > 9 {
            leftOver = 1
        } else {
            leftOver = 0
        }
        s := strconv.Itoa(sum%10)
        val := []rune(s)
        res = append(res, val...)
        p1--
    }
    
    for p2 >= 0 {
        digit2, _ := strconv.Atoi(string(digits2[p2]))
        
        sum := digit2 + leftOver
        if sum > 9 {
            leftOver = 1
        } else {
            leftOver = 0
        }
        s := strconv.Itoa(sum%10)
        val := []rune(s)
        res = append(res, val...)
        p2--
    }
    
    if leftOver != 0 {
        s := strconv.Itoa(leftOver)
        val := []rune(s)
        res = append(res, val...)
    }
    
    slices.Reverse(res)
    return string(res)
}