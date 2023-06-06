import java.util.Arrays;
import java.util.Stack;

public class DailyTemperatures {
    public int[] dailyTemperatures(int[] temperatures) {
        int[] answer = new int[temperatures.length];
        Stack<Integer> lowerTemps = new Stack<>();

        int i = 0;
        for (int temp: temperatures){
            while (!lowerTemps.isEmpty() && temperatures[lowerTemps.peek()] < temp)
                answer[lowerTemps.peek()] = i - lowerTemps.pop();

            lowerTemps.push(i);
            i++;
        }

        return answer;
    }


    public static void main(String[] args) {
        DailyTemperatures dt = new DailyTemperatures();
        int[] temperatures = {30,40,50,60};
        System.out.println(Arrays.toString(dt.dailyTemperatures(temperatures)));
    }

}
