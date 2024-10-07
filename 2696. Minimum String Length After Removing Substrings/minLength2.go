package MinLengthAfterRemove


// O(n) time,
// O(n) space,
// Approach: stack, 
func minLength2(s string) int {
    stack := []string{}
    for _, byteChar := range s {
        letter := string(byteChar)
        if len(stack) > 0 && (letter == "D" && stack[len(stack)-1] == "C" ||
        letter == "B" && stack[len(stack)-1] == "A") {
            stack = stack[:len(stack)-1]
        } else {
            stack = append(stack, letter)
        }
    }
    
    return len(stack)
}