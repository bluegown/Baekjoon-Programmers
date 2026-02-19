class Solution {
    public int[] solution(int[] arr) {
        if(arr.length == 1){
            return new int[]{-1};
        }
        int[] answer = new int[arr.length - 1];
        int min = arr[0];
        for (int elem: arr){
            if (elem < min){
                min = elem;
            }
        }
        int idx = 0;
        for(int i = 0; i< arr.length; i++){
            if(min!= arr[i]){
                answer[idx] = arr[i];
                idx++;
            }
        }
        return answer;
    }
}