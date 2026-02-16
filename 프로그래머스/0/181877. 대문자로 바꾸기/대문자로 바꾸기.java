class Solution {
    public String solution(String myString) {
        String answer = "";
        for(int i = 0; i< myString.length(); i++){
            char ch = myString.charAt(i);
            
            if(Character.isLowerCase(ch)){
                answer += Character.toUpperCase(ch);
            }else{
                answer += ch;
            }
        }
        return answer;
    }
}