import java.util.*;
import java.io.*;

public class Main {
    static int n, ans;
    static PriorityQueue<Integer> pq = new PriorityQueue<>();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        n = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine(), " ");
        for(int i = 0; i < n; i++) {
            pq.offer(Integer.parseInt(st.nextToken()));
        }

        while (true) {
            if(pq.size() >= 2) {
                int a = pq.poll();
                int b = pq.poll();
                ans += (a + b);
                pq.offer(a + b);
            } else {
                break;
            }
        }

        System.out.println(ans);
    }
}