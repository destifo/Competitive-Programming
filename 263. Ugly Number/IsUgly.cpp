class Solution {

// O(logn) time,
// O(1) space,
// Approach: math, numerics
public:
    
    int reduceByFactor(int num, int factor) {
        while (num != 0 && num % factor == 0){
            num /= factor;
        }
        
        return num;
    }
    
    bool isUgly(int n) {
        int factors[] = {2, 3, 5}; 
        
        for (int factor : factors) {
            // int factor = factors[i];
            n = reduceByFactor(n, factor);
        }
        
        return n == 1;
    }
};