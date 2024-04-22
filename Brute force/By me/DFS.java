import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

public class DFS {
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

        // Perform DFS starting from vertex 0
        DFS(graph, 0);
    }

    public static void DFS(int[][] G, int start) { 
        PreVisit(G, start); // indicate we have 'visited' the starting vertex
        G[start][start] = VISITED; // Mark the starting vertex as visited in the adjacency matrix
        int[] nList = G[start]; // obtaining neighbours of starting index

        for (int i=0; i<nList.length; i++) { // iterate over neighbours
        // Check if there is an edge from the starting vertex to vertex i and if vertex i is not visited
            if (nList[i] == 1 && G[i][i] != VISITED) {
                DFS(G, i); // search the neighbouring list
            }
        }
        // Call the PostVisit method to indicate finishing visiting the starting vertex
        PostVisit(G, start);

    }

    // Placeholder method for PreVisit
    public static void PreVisit(int[][] G, int v) {
        System.out.println("Pre-visiting node: " + v);
    }

    // Placeholder method for PostVisit
    public static void PostVisit(int[][] G, int v) {
        System.out.println("Post-visiting node: " + v);
    }
}
