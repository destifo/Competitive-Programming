

import "strings"


// O(n) time,
// O(n) space,
// Approach: string, array, 
func reverseWords(s string) string {
    
    words := strings.Fields(s);
    
    mid := len(words)/2;
    for i := 0; i < mid; i++ {
        temp := words[i];
        words[i] = words[len(words)-i-1];
        words[len(words)-i-1] = temp;
    }
    
    answer := strings.Join(words[:], " ");
    return answer;
}