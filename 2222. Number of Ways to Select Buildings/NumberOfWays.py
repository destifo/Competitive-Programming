class Solution:    
    
    def numberOfWays(self, s: str) -> int:
        prefixes = [[0, 0] for _ in range(len(s))] 
        for i in range(len(s)):
            zero_count = prefixes[i][0] + 1 if s[i] == "0" else 0
            one_count = prefixes[i][1] + 1 if s[i] == "1" else 0

            if i > 0:
                zero_count += prefixes[i - 1][0]
                one_count += prefixes[i - 1][1]
            
            prefixes[i] = [zero_count, one_count]         

        res = 0
        for i in range(len(s)):
            if s[i] == "0":
                res += prefixes[i][1] * (prefixes[-1][1] - prefixes[i][1])
            elif s[i] == "1":
                res += prefixes[i][0] * (prefixes[-1][0] - prefixes[i][0])

        return res