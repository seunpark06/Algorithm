import java.util.*;

public class Main {
    static ArrayList<Integer>[] graph;
    static boolean[] visited; //방문 기록용 배열
    static int count= 0; //바이러스 감염된 컴퓨터 수

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); // 전체 컴퓨터 수
        int m = sc.nextInt(); // 연결된 노드 수
        
        // 배열 할당
        graph = new ArrayList[n+1];
        visited = new boolean[n+1];

        for(int i = 1; i <= n; i++){
            graph[i] = new ArrayList<>();
        }
        // 연결 노드 기록
        for (int i = 0 ; i < m; i++){
            int a = sc.nextInt(), b = sc.nextInt();
            graph[a].add(b);
            graph[b].add(a);
        }

        dfs(1);
        System.out.println(count -1);
    }

    static void dfs(int node){
        count++;
        visited[node] = true; //방문 표시

        for (int next: graph[node]){ //아직 방문하지 않고 연결된 노드라면
            if(!visited[next]){
                dfs(next);
            }
        }
    }
}