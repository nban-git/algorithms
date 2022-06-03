package org.orchid.common;

import java.util.ArrayList;
import java.util.List;

public class EdgeWeightedGraph {

    private final int n;
    private final List<Edge>[] adj;

    public EdgeWeightedGraph(int n) {
        this.n = n;
        this.adj = new ArrayList[n];
        for (int i=0; i<n; i++) {
            adj[i] = new ArrayList<Edge>();
        }
    }

    public void addEdge(Edge e) {
        int v = e.either(), w = e.other(v);
        adj[v].add(e);
        adj[w].add(e);
    }

    public Iterable<Edge> adj(int v) {
        return adj[v];
    }

    public int V() {
        return n;
    }

    public int E() {
        return 0;
    }

    public String toString() {
        return "";
    }
}
