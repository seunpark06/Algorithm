import java.util.*;
import java.math.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        
        // 완료일 계산
        int[] complete = new int[progresses.length];
        for(int i = 0; i<progresses.length; i++){
            complete[i] = (int)Math.ceil((double)(100 - progresses[i]) / speeds[i]);
        }
        
        List<Integer> list = new ArrayList<>();
        int prev = complete[0];
        int count = 1;
        for(int j = 1; j<complete.length; j++){
            if(prev < complete[j]){
                prev = complete[j];
                list.add(count);
                count = 1;
            }else{
                count++;
            }
        }
        list.add(count); //마지막 배포기능
        
        int[] answer = new int[list.size()];
        for(int d=0; d<answer.length; d++){
            answer[d] = list.get(d);
        }
        return answer;
    }
}