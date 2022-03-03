import java.util.Collections;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;

public class LeastInterval {
    
    //used max priorityQueue to handle the priority for the tasks to be handled and
    //and normal queue to process the cooldown time of each task.
    public int leastInterval(char[] tasks, int n) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        Queue<Integer> waitingQueue = new LinkedList<>();
        Queue<Integer> queueTime = new LinkedList<>();
        int time = 0;

        int[] charCount = new int[26];
        for (char ch:tasks)
            charCount[ch-'A']++;

        for (int num:charCount)
            if (num != 0)
                pq.add(num);
        
        while (!pq.isEmpty() || !waitingQueue.isEmpty()){
            time++;

            if (!pq.isEmpty()){
                int cnt = pq.poll() - 1;
                if (cnt != 0){
                    waitingQueue.add(cnt);
                    queueTime.add(time + n);
                }
            }

            if (!waitingQueue.isEmpty()){
                if (queueTime.peek() == time){
                    queueTime.remove();
                    int popped = waitingQueue.remove();
                    pq.add(popped);
                }
            }
        }

        return time;
    }

    public static void main(String[] args){

        LeastInterval li = new LeastInterval();
        char[] tasks = new char[]{'A','A','A','A','A','A','B','C','D','E','F','G',};
        System.out.println(li.leastInterval(tasks,2)); 

    }
    
}
