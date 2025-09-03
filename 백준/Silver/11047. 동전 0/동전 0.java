

import java.util.*;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int k = sc.nextInt();

        int[] coins = new int[n];

        for(int i = 0; i < n ; i++){
            coins[i] = sc.nextInt();
        }

        int count = 0;
        for(int d = n-1; d >=0 ; d--){
            count += k / coins[d]; //몫
            k %= coins[d]; //나머지
        }
        System.out.println(count); //결과출력
    }

}