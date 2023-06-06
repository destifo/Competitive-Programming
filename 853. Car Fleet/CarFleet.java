import java.util.Arrays;
import java.util.Stack;

public class CarFleet {
    //solution without stack
    public int carFleet(int target, int[] position, int[] speed) {
        int carsNum = position.length;
        double[][] positionTimePair = new double[carsNum][2];
        double lastCarTime = Double.MIN_VALUE;
        int fleetNumber = 1;

        for (int i = 0; i < carsNum; i++){
            double[] pair = {position[i], (target - position[i])/(double)speed[i]};
           positionTimePair[i] = pair;
        }

        Arrays.sort(positionTimePair, (a, b) -> (int)a[0] - (int)b[0]);

        for (int i = carsNum - 1; i >= 0; i--){
            double currentTime = positionTimePair[i][1];
            if (lastCarTime == Double.MIN_VALUE)
                lastCarTime = (currentTime);
            if (currentTime > lastCarTime){
                lastCarTime = (currentTime);
                fleetNumber++;
            }
        }

        return fleetNumber;
    }




    //solution with stack
    public int carFleet2(int target, int[] position, int[] speed) {
        int carsNum = position.length;
        double[][] positionTimePair = new double[carsNum][2];
        Stack<double[]> fleets = new Stack<>();

        for (int i = 0; i < carsNum; i++){
            double[] pair = {position[i], (target - position[i])/(double)speed[i]};
           positionTimePair[i] = pair;
        }

        Arrays.sort(positionTimePair, (a, b) -> (int)a[0] - (int)b[0]);

        for (int i = carsNum - 1; i >= 0; i--){
            double currentTime = positionTimePair[i][1];
            if (fleets.isEmpty())
                fleets.push(positionTimePair[i]);
            if (!fleets.isEmpty() &&  currentTime > fleets.peek()[1]){
                fleets.push(positionTimePair[i]);
            }
        }

        return fleets.size();
    }



    public static void main(String[] args) {
        //int[][] trials = {{2,1}, {1, 2}};
        //Arrays.sort(trials, (a, b) -> a[0] - b[0]);
        //System.out.println(Arrays.deepToString(trials));

        CarFleet cf = new CarFleet();
        int target = 10;
        int[] position = {6, 8};
        int[] speed = {3,2};
        System.out.println(cf.carFleet(target, position, speed));
    }
}
