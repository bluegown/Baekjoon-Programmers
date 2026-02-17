import java.util.Arrays;
import java.util.Collections;
class Solution {
    public int[] solution(long n) {
        String num = Long.toString(n); // Long -> String
        
        String[] ans = num.split("");
        int[] answer = new int[ans.length];
        
        for(int i = 0 ; i< ans.length; i++){
            answer[i] = Integer.parseInt(ans[ans.length - i - 1]);
        }
        
        return answer;
        
    }
}