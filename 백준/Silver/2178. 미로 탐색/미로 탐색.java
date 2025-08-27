

import java.util.*;

public class Main {
    static int n, m;
    static int[][] maze, dist;
    static int[] dx = {0, 1, 0, -1}, dy = {1, 0, -1, 0};
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        sc.nextLine();
        maze = new int[n][m];
        dist = new int[n][m];

        for(int i = 0; i < n ; i++){
            String s = sc.nextLine();
            for(int j = 0; j < m ; j++){
                maze[i][j] = s.charAt(j) - '0'; //문자를 실제 숫자 값으로 변환
            }
        }

        dfs(0,0);
        System.out.println(dist[n-1][m-1]);

    }

    static void dfs(int x, int y){
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{x, y});
        dist[x][y] = 1; //시작 위치도 포함

        while(!q.isEmpty()){
            int[] now = q.poll();

            for(int d = 0; d < 4; d++){
                int nx = now[0] + dx[d];
                int ny = now[1] + dy[d];

                if(nx >= 0 && ny >= 0 && nx < n && ny < m){
                    if(maze[nx][ny] == 1 && dist[nx][ny] == 0){
                        q.offer(new int[]{nx, ny});
                        dist[nx][ny] = dist[now[0]][now[1]] + 1;
                    }

                }
            }
        }
    }
}