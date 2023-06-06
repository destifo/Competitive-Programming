import "math";


// O(sum(len(str) for str in strs)) time,
// O(1) space,
// Approach: vertical scanning, 
func longestCommonPrefix(strs []string) string {
    min_len := 201;
    
    for _, str := range strs {
        curr_len := float64(len(str));
        min_len = int(math.Min(float64(min_len), curr_len));
    }
    
    prefix_index := 0;
    for i := 0; i < min_len; i++ {
        curr_char := []rune(strs[0])[i];
        for _, str := range strs {
            char := []rune(str)[i]
            if char != curr_char {
                return string([]rune(strs[0])[:prefix_index]);
            }
        }
        prefix_index += 1;
    }
    if min_len == 0 {
        return "";
    }
    
    return string([]rune(strs[0])[:prefix_index]);
}