import java.util.*;

public class Solution {
    public int solution(int n) {
        int answer = 0;
        String num = Integer.toString(n);
        String arr[] = num.split(""); // String -> StringArray
        for(int i = 0; i < arr.length; i++){
            answer = answer + Integer.parseInt(arr[i]);
        }

        return answer;
    }
}