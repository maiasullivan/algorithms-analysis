import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

public class BFS {
    public static final int VISITED = 1;

    public static void main(String[] args) {
        // Create a sample graph
        int[][] graph = {
            {0, 1, 1, 0, 0},
            {1, 0, 0, 1, 0},
            {1, 0, 0, 1, 1},
            {0, 1, 1, 0, 1},
            {0, 0, 1, 1, 0}
        };

        // Perform BFS starting from vertex 0
        BFS(graph, 0);
    }

    public static void BFS(int[][] G, int start) { // start integer is from where we begin traversal
        int n = G.length;
        boolean visited[] = new boolean[n];
        Queue<Integer> queue = new LinkedList<>();

        queue.offer(start);
        visited[start] = true; // set start value to visited

        while (!queue.isEmpty()) {
            int vertex = queue.poll(); // head of queue is retrived and removed
            System.out.println("Visited: " + vertex); // Indicates the vertex is visited
            
            for (int i = 0; i < n; i++) {
                if (G[vertex][i] == 1 && !visited[i]) {
                    queue.offer(i);
                    visited[i] = true;
                }
            }
        }

    }

}

