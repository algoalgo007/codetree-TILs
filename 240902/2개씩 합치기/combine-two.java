import java.util.*;
import java.io.*;

public class Main {
    static int n;
    static Long ans = 0L;
    static PriorityQueue<Long> pq = new PriorityQueue<>();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        n = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine(), " ");
        for(int i = 0; i < n; i++) {
            pq.offer(Long.parseLong(st.nextToken()));
        }

        while (true) {
            if(pq.size() >= 2) {
                Long a = pq.poll();
                Long b = pq.poll();
                ans += (a + b);
                pq.offer(a + b);
            } else {
                break;
            }
        }

        System.out.println(ans);
    }
}