import java.util.*;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        sc.nextLine(); //줄넘김 제거


        Set<String> set = new HashSet<String>();

        for(int i = 0; i <num ; i++){
            set.add(sc.nextLine());
        }

        // 정렬을 위해 Array로 변환
        List<String> sort_str = new ArrayList<>(set);
        sort_str.sort((a,b) -> {
            if (a.length() != b.length()) return a.length() - b.length();
            return a.compareTo(b);
        });

        // a.length() - b.length() 가 양수면 a가 뒤로 감
        // a.length() - b.length() 가 음수면 a가 앞으로 감
        
        //a.compareTo(b) 사전 순서대로 비교

        for (String s: sort_str){
            System.out.println(s);
        }
    }
}