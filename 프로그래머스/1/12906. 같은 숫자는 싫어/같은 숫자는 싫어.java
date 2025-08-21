import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        
        List<Integer> list = new ArrayList<>();
        // 직전 숫자와 비교해서 같은 값이면 제거한다
        int prev = -1; //이전 숫자를 담을 값
        for(int i = 0; i < arr.length ; i++){
            if(prev != arr[i]){
                list.add(arr[i]);    
            }
            prev = arr[i];
        }
        // 리스트를 배열로 변환
        int[] answer = new int[list.size()];
        for(int i = 0; i< list.size() ; i++){
            answer[i] = list.get(i);
        }

        return answer;
    }
}