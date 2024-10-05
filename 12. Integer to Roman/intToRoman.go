package IntToRoman


// O(1) time,
// O(1) space,
// Approach: map, 
func intToRoman(num int) string {
        
    ones := []string{"","I","II","III","IV","V","VI","VII","VIII","IX"}
    tens := []string{"","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"}
    hundreds := []string{"","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"}
    thousands := []string{"","M","MM","MMM"}
    
    return thousands[num/1000]+hundreds[(num%1000)/100]+tens[(num%100)/10]+ones[num%10]
}