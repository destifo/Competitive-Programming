


def findMin(s):
    window = dict()
    window['1'] = 0
    window['2'] = 0
    window['3'] = 0
    m = len(s)
    l, r = 0, 0
    min_len = float('inf')

    while r < m:
        window[s[r]] +=1
        if window['1'] > 0 and window['2'] > 0 and window['3'] > 0:
            min_len = min(min_len, r-l+1)
            while window['1'] > 0 and window['2'] > 0 and window['3'] > 0:
                min_len = min(min_len, r-l+1)
                window[s[l]] -=1
                l +=1
            min_len = min(min_len, r-l+2)
        
        r+=1

    return min_len if min_len != float('inf') else 0

# print(findMin('122321'))
n = int(input())
for i in range(n):
    s = input()
    print(findMin(s))