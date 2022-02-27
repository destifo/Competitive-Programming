class Solution:
    operators = ["+", "-", "*", "/"]
    def evalRPN(self, tokens) -> int:
        stack = []

        for ch in tokens:
            if ch in self.operators:
                secondOperand = stack.pop()
                firstOperand = stack.pop()

                result = self.evalExpression(firstOperand, secondOperand, ch)
                stack.append(result)
            else:
                stack.append(int(ch))
        
        return stack.pop()


    def evalExpression(self, first, second, operator):
        if operator == '+':
            return first + second
        elif operator == '-':
            return first - second
        elif operator == '*':
            return first * second
        else:
            return int(first/second)


sol = Solution()

print(sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
        