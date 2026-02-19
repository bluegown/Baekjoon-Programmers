class Solution {
    public String solution(String s) {
        String answer = "";
        
        int len = s.length();
        
        if (len % 2 == 0){ // 길이 4면 1부터 2까지
            return s.substring(len / 2 - 1, (len / 2) + 1);
        }else{ // 길이 5면 // 2
            return s.substring(len / 2, (len / 2) + 1);
        }
    }
}