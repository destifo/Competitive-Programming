import java.util.Arrays;
import java.util.List;
import java.util.Stack;

class Solution {
    private Stack<Integer> stack = new Stack<>();
    private final List<String> operators = Arrays.asList("+", "-", "*", "/");


    
    public int evalRPN(String[] tokens) {

        for (String ch: tokens){
            if (operators.contains(ch)){
                int secondOperand = stack.pop();
                int firstOperand = stack.pop();

                int result = evaluateExpression(firstOperand, secondOperand, ch);
                stack.push(result);
            }else{
                stack.push(Integer.parseInt(ch));
            }


        }

        return stack.pop();
        
    }

    private int evaluateExpression(int first, int second, String operator){
        if (operator == "+")
            return first + second;
        else if (operator== "-")
            return first - second;
        else if (operator == "*")
            return first * second;
        else
            return first/second;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        String[] tokens = new String[]{"2","1","+","3","*"};

        System.out.println(sol.evalRPN(tokens));
    }

}