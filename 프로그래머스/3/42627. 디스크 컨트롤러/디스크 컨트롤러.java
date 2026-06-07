import java.util.*;

class Solution {
    public int solution(int[][] jobs) {
        int answer = 0;
        int i = 0;
        int start = -1;
        int now = 0;
        
        PriorityQueue<int[]> heap = new PriorityQueue<>((o1,o2) -> Integer.compare(o1[0],o2[0]));

        while( i < jobs.length) {
            for (int [] j : jobs){
                if (start < j[0] && j[0] <= now){
                    heap.offer(new int[]{j[1],j[0]});
                }
            }
            if(!heap.isEmpty()){
                int [] current = heap.poll();
                int l = current[0];
                int s = current[1];
                start = now;
                now += l;
                answer += (now - s);
                i++;
            }else{
                now++;
            }
        }
        

        return answer / jobs.length;
    }
}