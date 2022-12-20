import "strings";


// O(n) time, n --> number of letters in pattern
// O(n) space,
// Approach: string, hashmap, 
func wordPattern(pattern string, s string) bool {
 
    pattern_match := make(map[rune]string);
    used := make(map[string]bool);
    
    words := strings.Split(s, " ");
    if len(words) != len(pattern) {
        return false;
    }
    
    for i, letter := range pattern {
        word := words[i];
        matched_word, exist := pattern_match[letter];
        
        if exist && matched_word != word {
            return false
        } else if !exist {
            if _, ok := used[word]; ok {
                return false;
            }
            pattern_match[letter] = word;
            used[word] = true;
        }  
    }
    
    return true; 
}