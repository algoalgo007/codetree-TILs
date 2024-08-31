import java.io.*;
import java.util.*;

public class Main {
    public static int[][] arr;
    public static int N, M, K;
    public static int[][] copyArr;
    public static int startX, startY, endX, endY, count;

    public static void rotate() {
        copyArr = new int[N][M];
        for(int i = 0; i < N; i++)
            for(int j = 0; j < M; j++)
                copyArr[i][j] = arr[i][j];
        
        int count = Math.min(N/2, M/2);
        for(int c = 0; c < count; c++) { //라인 전부 돌리기
            int val = copyArr[startX+c][startY+c];
            
            for(int j = startY + c; j < endY - c; j++) { //위쪽
                copyArr[startX + c][j] = copyArr[startX + c][j + 1];
            }
            for(int j = startX + c; j < endX - c; j++) { //오른쪽
                copyArr[j][endY - c] = copyArr[j + 1][endY - c];
            }
            for(int j = endY - c; j > startY + c; j--) { //아래쪽
                copyArr[endX - c][j] = copyArr[endX - c][j - 1];
            }     
            for(int j = endX - c; j > startX + c; j--) { //왼쪽
                copyArr[j][startY + c] = copyArr[j - 1][startY + c];
            }
            copyArr[startX + c + 1][startY + c] = val;
        }
        arr = copyArr;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        StringBuilder sb = new StringBuilder();

        arr = new int[N][M];

        for(int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < M; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        
        startX = 0; startY = 0;
        endX = N-1; endY = M - 1;
        for(int i = 0; i < K; i++) {
        	rotate();
        }
        for(int[] ar : arr) {
        	for(int x : ar) {
                sb.append(x + " ");
        	}
        	sb.append("\n");
        }
        System.out.print(sb);
        br.close();
    }
}