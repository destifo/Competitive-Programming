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
