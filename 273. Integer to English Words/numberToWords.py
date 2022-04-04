'''
https://leetcode.com/problems/integer-to-english-words/submissions/
'''

class Solution:
    belowTwenty = {
            1:" One", 2:" Two", 3:" Three",
            4:" Four",5:" Five",6:" Six",7:" Seven",
            8:" Eight",9:" Nine",10:" Ten",11:" Eleven",
            12:" Twelve",13:" Thirteen",14:" Fourteen",
            15:" Fifteen", 16:" Sixteen", 17:" Seventeen",
            18:" Eighteen", 19:" Nineteen"
        }

    tenth = {
            20:" Twenty", 30:" Thirty", 40:" Forty",
            50:" Fifty", 60:" Sixty", 70:" Seventy",
            80:" Eighty", 90:" Ninety"
        }

    powerOfTen = [
        "Thousand", "Million", "Billion"
        ]

    def numberToWords(self, num: int):
        if num == 0:
            return "Zero"
        return self.numberToWords1(num, 0).strip()
    
    def numberToWords1(self, num: int, power):
        if num == 0:
            return ''
        if num < 1000 and power == 0:
            return self.numberToWordsLessThanThousand(num)
        if num < 1000 and power == 1:
            return self.numberToWordsLessThanThousand(num) + " Thousand"
        if num < 1000 and power == 2:
            return self.numberToWordsLessThanThousand(num) + " Million"
        if num < 1000 and power == 3:
            return self.numberToWordsLessThanThousand(num) + " Billion"
        

        return self.numberToWords1(num//1000, power + 1) + self.numberToWords1(num%1000, power)
    

    def numberToWordsLessThanThousand(self, num):
        hundredth = num//100
        tenth = num % 100
        ones = num % 10

        numStr = ""
        if hundredth > 0:
            numStr += (self.belowTwenty[hundredth] + " Hundred") 

        if tenth < 20 and tenth > 0:
            numStr += self.belowTwenty[tenth]
            return numStr
        
        if tenth >= 20:
            numStr += self.tenth[tenth-ones]
        if ones > 0:
            numStr += self.belowTwenty[ones]

        # numStr.lstrip()
        return numStr


sol = Solution()
print(sol.numberToWords(1000000))