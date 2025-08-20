import java.util.*;

public class Main {
    static ArrayList<Integer>[] graph;
    static boolean[] visited;
    static int count;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); // 컴퓨터 수
        int m = sc.nextInt(); // 연결 수

        graph = new ArrayList[n + 1];
        visited = new boolean[n + 1];

        for (int i = 1; i <= n ; i++) graph[i] = new ArrayList<>();

        for (int i = 0; i < m; i++){
            int a = sc.nextInt(), b = sc.nextInt();
            graph[a].add(b);
            graph[b].add(a);
        }
        
        dfs(1);
        System.out.println(count - 1); //1번 컴퓨터 제외
        
    }
    
    static void dfs(int node){
        visited[node] = true;
        count++;
        
        for(int next: graph[node]){
            if(!visited[next]){
                dfs(next);
            }
        }
    }
}