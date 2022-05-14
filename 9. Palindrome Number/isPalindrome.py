import math


class Solution:
    def isPalindrome(self, x: int):
        # without converting to string
        if x > 0:
            digits = int(math.log10(x))+1
        elif x == 0:
            digits = 1
        else:
            return False
        def isPali(divd_pow, mod_pow):
            if divd_pow <= mod_pow:
                return True

            qutnt = x % (10 ** (divd_pow + 1))
            qutnt = qutnt//(10 **divd_pow)
            rem = x % (10 **(mod_pow + 1))
            rem = rem // (10**mod_pow)
            if qutnt != rem:
                return False

            return isPali(divd_pow - 1, mod_pow + 1)

        return isPali(digits - 1, 0)

sol = Solution()
print(sol.isPalindrome(112110))