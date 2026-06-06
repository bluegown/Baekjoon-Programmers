import java.util.*;
class Solution {
    boolean visited[];
    Queue<Integer> queue = new LinkedList<>();
    public int solution(int n, int[][] computers) {
        int answer = 0;
        visited = new boolean[computers.length];
        
        for(int i = 0; i < computers.length; i++){
            if(visited[i] == false){
                bfs(i, computers, computers.length);
                answer++;
            }
        }
        return answer;
    }
    
    void bfs(int i, int computers[][], int n){
        queue.offer(i); // 이게 여기선 append인가봐 신기하다..
        visited[i] = true;
        
        while(!queue.isEmpty()){
            int v = queue.poll();
            
            for (int j = 0; j < n; j++){
                if (visited[j] == false && computers[v][j] == 1){
                    visited[j] = true;
                    queue.offer(j);
                }
            }
        }
    }
}