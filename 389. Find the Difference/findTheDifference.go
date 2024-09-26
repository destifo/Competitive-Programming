package FindTheDifference



func ToMap(s string) map[rune]int {
    count := make(map[rune]int)
    
    chars := []rune(s)
    for _, char := range chars {
        count[char]++
    }
    
    return count
}


// O(n) time,
// O(n) space,
// Approach: counting, hashmap
func findTheDifference(s string, t string) byte {
    sMap := ToMap(s)
    tMap := ToMap(t)
    
    for char, count := range tMap {
        if count != sMap[char] {
            return byte(char)
        }
    }
    
    var b byte
    return b
}