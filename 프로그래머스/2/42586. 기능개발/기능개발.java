import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        
        
        // 완료일 계산
        
        int[] days = new int[progresses.length];
        for (int i = 0 ; i<progresses.length; i++){
            days[i] = (int)Math.ceil((100 - progresses[i] ) / (double)(speeds[i]));    
        }
        
        List<Integer> list = new ArrayList<>();
        int count = 0;
        int prev = days[0];
        for(int d=0; d < days.length ; d++){
            if(days[d] > prev){
                list.add(count);
                count = 1;
                prev = days[d];
            }
            else{
                count ++;
            }
        }
        list.add(count);
        
        int[] answer = new int[list.size()];
        for(int i = 0; i < list.size(); i++){
            answer[i] = list.get(i);
        }
        
        return answer;
    }
}