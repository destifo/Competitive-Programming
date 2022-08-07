class Solution:
    # O(n) time,
    # O(n) space,
    # Approach: dynamic programming,
    def countVowelPermutation(self, n: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        vowel_index = {
            'a' : 0,
            'e' : 1,
            'i' : 2,
            'o' : 3,
            'u' : 4,
        }
        
        vowel_span = {
            'a' : ['e', 'i', 'u'],
            'e' : ['a', 'i'],
            'i' : ['e', 'o'],
            'o' : ['i'],
            'u' : ['i', 'o']
        }
        
        dp = [ [1 for i in range(n)] for j in range(5) ]
        
        for i in range(1, n):
            for j in range(5):
                vowel = vowels[j]
                v_index = vowel_index[vowel]
                vowel_spanners = vowel_span[vowel]
                tot = 0
                for vp in vowel_spanners:
                    index = vowel_index[vp]
                    tot += dp[index][i-1]
                    
                dp[v_index][i] = tot
                
        result = 0
        for i in range(5):
            result +=dp[i][n-1]
                    
        return result % ((10**9) + 7)