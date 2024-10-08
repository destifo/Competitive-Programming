package MinSwapsToMakeBalancedString

func shiftRightToOpeningBracket(chars []rune, index int) int {
	for index >= 0 && byte(chars[index]) != '[' {
		index -= 1
	}

	return index
}

// O(n) time,
// O(n) space,
// Approach: counting, two pointers
func minSwaps(s string) int {
	chars := []rune(s)
	lastOpeningIndex := shiftRightToOpeningBracket(chars, len(s)-1)

	closings := 0
	swaps := 0
	for i := 0; i < len(s); i++ {
		curr := chars[i]
		if curr == ']' {
			closings += 1
		} else {
			closings -= 1
		}
		if closings > 0 {
			swaps += 1
			closings -= 2
			chars[i], chars[lastOpeningIndex] = chars[lastOpeningIndex], chars[i]
			lastOpeningIndex = shiftRightToOpeningBracket(chars, lastOpeningIndex)
		}
	}

	return swaps
}


// O(n) time,
// O(n) space,
// Approach: stack,
func minSwaps2(s string) int {
    
    stack := []string{}
    unbalanced := 0
    
    for i := 0; i < len(s); i++ {
        char := string(s[i])
        if char == "[" {
            stack = append(stack, char)
        } else {
            if len(stack) > 0 {
                stack = stack[:len(stack)-1]
            } else {
                unbalanced += 1
            }
        }
    }
    
    return (unbalanced + 1)/2
}