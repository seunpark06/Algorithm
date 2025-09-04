

import java.util.*;

public class Main {
    static ArrayList<Integer>[] graph;
    static boolean[] visited;
    static int count;

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();//컴퓨터 수
        int m= sc.nextInt();//연결된 컴퓨터 쌍의 수


        // 배열 할당
        graph = new ArrayList[n + 1];
        visited = new boolean[n + 1];

        //리스트 할당 (1번 노드부터 N번 노드)
        for(int i=1; i<n+1; i++) graph[i] = new ArrayList<>();

        for(int i = 0; i < m; i++){
            int a = sc.nextInt();
            int b = sc.nextInt();
            graph[a].add(b);// 연결된 노드
            graph[b].add(a);
        }

        dfs(1);
        System.out.println(count-1);



    }
    static void dfs(int node){
        visited[node] = true;
        count++;

        for(int next: graph[node]){
            if(!visited[next]) dfs(next); //방문하지 않은 노드 방문
        }
    }

}