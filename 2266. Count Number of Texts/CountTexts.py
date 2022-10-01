class Solution:
    # O(n) time,
    # O(n) space,
    # Approach: dp top-down, memoization
    def countTexts(self, pressedKeys: str) -> int:
        key_ch = {2: 3, 3: 3, 4: 3, 5: 3, 6: 3, 7: 4, 8: 3, 9: 4}
        memo = {}
        MOD = (10**9) + 7
        
        def findDecodings(num, count):
            if (count, num) in memo:
                return memo[(count, num)] 
            
            branches = key_ch[num]
            tot = 0
            for i in range(1, branches+1):
                if i < count:
                    tot += findDecodings(num, count-i)
                if i == count:
                    tot += 1
               
            memo[(count, num)] = (tot%MOD)
            return tot
          
        
        ways = 1
        window = []
        for ch in pressedKeys:
            if not window:
                window = [ch, 1]
                continue
            
            if window[0] == ch:
                window[1] +=1
            else:
                num = window[0]
                num = int(num)
                count = window[1]
                decodings = findDecodings(num, count)
                ways *= decodings
                ways %=MOD
                window = [ch, 1]
        
        num = window[0]
        num = int(num)
        count = window[1]
        decodings = findDecodings(num, count)
        ways *= decodings
        ways %=MOD
        
        return ways