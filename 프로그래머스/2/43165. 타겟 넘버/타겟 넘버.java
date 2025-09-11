class Solution {
    int answer = 0;
    public int solution(int[] numbers, int target) {
        dfs(numbers, target, 0, 0);
        return answer;
    }
    void dfs(int[] numbers, int target, int sum, int count){
        // 모든 숫자를 다 사용하면 리턴
        if(numbers.length == count){ //모든 수 사용
            if(target == sum){ //타겟넘버 도달
                answer++;
                return;
            }    
        }
        else{
            dfs(numbers, target, sum - numbers[count], count+1);
            dfs(numbers, target, sum + numbers[count], count+1);
        }
    }
}