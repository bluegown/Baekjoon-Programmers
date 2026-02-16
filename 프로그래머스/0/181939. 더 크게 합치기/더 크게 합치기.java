class Solution {
    public int solution(int a, int b) {
        int answer = 0;

        
        String ch1 = Integer.toString(a);
        String ch2 = Integer.toString(b);
        
        if(Integer.parseInt(ch1 + ch2) >= Integer.parseInt(ch2 + ch1)){
            return Integer.parseInt(ch1 + ch2);
        }
        return Integer.parseInt(ch2 + ch1);
    }
}