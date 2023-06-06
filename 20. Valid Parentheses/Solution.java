/** 
 https://leetcode.com/problems/valid-parentheses/
*/

import java.util.HashMap;
import java.util.Stack;
import java.util.Map.Entry;

class Solution {
    public boolean isValid(String s) {
        HashMap<Character, Character> brackets = new HashMap<>();
        brackets.put('<', '>');
        brackets.put('(', ')');
        brackets.put('[', ']');
        brackets.put('{', '}');

        Stack<Character> stack = new Stack<>();

        for (char ch: s.toCharArray()){
            if (brackets.containsKey(ch)){
                stack.push(ch);
                continue;
            }
                
            if (brackets.containsValue(ch)){
                for (Entry<Character, Character> entry:brackets.entrySet()){
                    if (entry.getValue() == ch){
                        if (stack.isEmpty())
                            return false;
                        var brckt = stack.pop();
                        if (brckt != entry.getKey())
                            return false;
                    }
                }
            }
            
        }

        if (stack.size() == 0)
            return true;
        return false;
        
    }
}