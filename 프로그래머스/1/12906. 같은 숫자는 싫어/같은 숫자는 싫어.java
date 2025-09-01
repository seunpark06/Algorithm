import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        
        List<Integer> list = new ArrayList<>();
        int prev = arr[0];
        list.add(arr[0]); // 첫번째 값을 넣어준다
        for(int i = 1; i < arr.length; i++){
            if(prev != arr[i]){ // 배열의 이전 요소랑 비교
                prev = arr[i];
                list.add(arr[i]);
            }
        }
        
        int[] answer = new int[list.size()];
        for(int d=0; d<list.size() ; d++){
            answer[d] = list.get(d);
        }
        

        return answer;
    }
}