import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        List<String> list = new ArrayList<>();
        for(String p : phone_book){
            list.add(p);
        }
        
        // 정렬
        Collections.sort(list);
        
        for(int i=0; i<list.size()-1;i++){
            if(list.get(i+1).startsWith(list.get(i))){
                return false;    
            }            
            
        }
        
        return true;
    }
}