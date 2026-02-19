class Solution {
    public String solution(String s) {
        String answer = "";
        
        String a[] = s.split(" ");
        
        int arr[] = new int[a.length];
        
        
        int max = Integer.parseInt(a[0]);
        int min = Integer.parseInt(a[0]);
        for(int i = 0; i< a.length; i++){
            if(max <  Integer.parseInt(a[i])){
                max = Integer.parseInt(a[i]);
            }
            if(min > Integer.parseInt(a[i])){
                min = Integer.parseInt(a[i]);
            }
        }
        StringBuilder sb = new StringBuilder();
        sb.append(min);
        sb.append(" ");
        sb.append(max);
        
        return sb.toString();
    }
}