class Solution {
    public boolean solution(int x) {
        boolean answer = true;
        
        String num = Integer.toString(x); // int -> String으로 교체
        
        String[] arr = num.split(""); // String -> StringArr으로 변경
        int sum = 0;
        for(String s: arr){
            sum = sum + Integer.parseInt(s);
        }
        if(x % sum == 0){
            return true;
        }else{
            return false;
        }
    }
}