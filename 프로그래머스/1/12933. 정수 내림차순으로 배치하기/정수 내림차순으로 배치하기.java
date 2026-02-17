import java.util.Arrays;
import java.util.Collections;
class Solution {
    public long solution(long n) {
        long answer = 0;
        String str = Long.toString(n); // 1. long -> String으로 자료형 변환
        // 2. 문자열을 문자 배열로 변환
        String[] arr = str.split("");
        
        Arrays.sort(arr, Collections.reverseOrder());
        
        StringBuilder sb = new StringBuilder();
        for (String s: arr){
            sb.append(s);
        }
        
        return Long.parseLong(sb.toString());
    }
}