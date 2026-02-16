class Solution {
    public String solution(String my_string, int k) {
        String answer = "";
        StringBuffer answerBuffer = new StringBuffer();
        for(int i = 0; i< k ;  i++){
            answerBuffer.append(my_string);
        }
        return answerBuffer.toString();
    }
}