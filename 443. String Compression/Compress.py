class Solution:
    def compress(self, chars):
        n = len(chars)
        s = ''
        if n == 1:
            s += chars[0]
            return n
        l = 0
        r = 1
        while r <= n:
            length = 1
            char = chars[l]
            while r < n and chars[r] == char:
                r += 1
                length +=1

            if length == 1:
                s += char
            else:
                s += char
                s += str(length)

            l = r
            r += 1

        index = 0
        for ch in s:
            chars[index] = ch
            index +=1

        for i in range(n - 1, index - 1, -1):
            chars.pop(i)
            

        return len(chars)