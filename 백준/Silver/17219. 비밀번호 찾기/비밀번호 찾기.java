import java.util.*;

public class Main {
    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt(); //저장된 사이트 수
        int m = scan.nextInt(); //찾으려는 비밀번호 수

        Map<String, String> map = new HashMap<>();
        for(int i = 0; i < n; i++){
            map.put(scan.next(), scan.next());
        }

        for(int i = 0; i < m; i++){
            System.out.println(map.get(scan.next()));
        }
    }
}