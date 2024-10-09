package MinAddToMakeValid

// O(n) time,
// O(n) space,
// Approach; stack
func minAddToMakeValid(s string) int {
	stack := []string{}

	moves := 0
	for _, char := range s {
		ch := string(char)

		if ch == "(" {
			stack = append(stack, ch)
		} else {
			if len(stack) > 0 {
				stack = stack[:len(stack)-1]
				continue
			}

			moves += 1
		}
	}

	return moves + len(stack)
}
