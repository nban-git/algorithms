package org.orchid;

import org.orchid.common.Edge;
import org.orchid.common.EdgeWeightedGraph;

import java.util.Comparator;
import java.util.PriorityQueue;

public class MinimumSpanningTree {

    class EdgeComparator implements Comparator<Edge> {
        public int compare(Edge e1, Edge e2) {
            return 0;
        }
    }

    private void insertTreesToPriorityQueue(EdgeWeightedGraph graph) {

    }

    public void kruskalMst(EdgeWeightedGraph graph) {
        PriorityQueue<EdgeWeightedGraph> pq = new PriorityQueue<>();
        insertTreesToPriorityQueue(graph);
    }
}
