import java.util.*;
import java.io.*;

public class Main {
    static int n, m;
    static int[] arr;
    static int[] arr2;
    static int answer = 0;
    static ArrayList<Integer> ans = new ArrayList<>();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        n = Integer.parseInt(st.nextToken());
        arr = new int[n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            arr[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine(), " ");
        m = Integer.parseInt(st.nextToken());
        arr2 = new int[m];
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            arr2[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(arr2);

        for(int i = 0; i < n - m + 1; i++) {
            ArrayList<Integer> temp = new ArrayList<>();
            for(int j = i; j < i + m; j++) {
                temp.add(arr[j]);
            }
            Collections.sort(temp);
            int val = arr2[0] - temp.get(0);
            boolean flag = true;
            for (int j = 0; j < m; j++) {
                if (arr2[j] - temp.get(j) != val) {
                    flag = false;
                }
            }
            if (flag) {
                answer += 1;
                ans.add(i + 1);
            }
        }

        System.out.println(answer);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < ans.size(); i++) {
            sb.append(ans.get(i));
            sb.append("\n");
        }
        System.out.print(sb);
    }
}