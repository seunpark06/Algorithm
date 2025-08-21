import java.util.*;

class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        
        List<Integer> max = new ArrayList<>();
        List<Integer> min = new ArrayList<>();
        // 큰 값 중에 제일 큰 값
        // 작은 값 중에 제일 큰 값
        for(int i = 0; i < sizes.length; i++){
            if(sizes[i][0] > sizes[i][1]){
                max.add(sizes[i][0]);  
                min.add(sizes[i][1]); 
            }else{
                max.add(sizes[i][1]);  
                min.add(sizes[i][0]); 
            }
            
            
        }
        
        Collections.sort(max);
        Collections.sort(min);
        Collections.reverse(max);
        Collections.reverse(min);
        System.out.println(max.get(0));   
        System.out.println(min.get(0));   
        answer = max.get(0) * min.get(0);
        return answer;
    }
}