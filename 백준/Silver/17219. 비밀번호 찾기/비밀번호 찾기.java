

import java.util.*;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int n = 0;
        int m = 0;
        n = sc.nextInt();
        m = sc.nextInt();

        Map<String, String> map = new HashMap<>();

        for(int i = 0; i < n; i++){
            map.put(sc.next(), sc.next());
        }

        for(int i = 0; i < m; i++){
            System.out.println(map.get(sc.next()));
        }
    }

}