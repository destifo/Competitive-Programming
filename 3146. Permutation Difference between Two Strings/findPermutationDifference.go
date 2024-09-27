package FindPermutationDifference

import "math"


func findPermutationDifference(s string, t string) int {
    locS, locT := make(map[rune]int), make(map[rune]int)
    
    for i, val := range s {
        locS[val] = i
    }
    
    for i, val := range t {
        locT[val] = i
    }
    
    diff := 0
    for key, loc := range locS {
        currDiff := loc-locT[key]
        diff += int(math.Abs(float64(currDiff)))
    }
    
    return diff
}