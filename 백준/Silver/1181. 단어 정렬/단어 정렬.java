import java.util.*;

public class Main {
    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        int total_num = scan.nextInt();
        scan.nextLine(); // 줄넘김 제거

        Set<String> set = new HashSet<>();
        for(int i = 0; i < total_num ; i++){
            set.add(scan.nextLine());
        }

        //정렬을 위해 리스트로 변환
        List<String> w_list = new ArrayList<>(set);

        w_list.sort((a,b) -> {
            if(a.length() != b.length()) return a.length() - b.length();
            return a.compareTo(b);
        });

        for(String s : w_list){
            System.out.println(s);
        }
    }
}