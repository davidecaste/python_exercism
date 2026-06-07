import java.util.Collections;
import java.util.Collection;
import java.util.Map;
import java.util.ArrayList;
import java.util.HashMap;

public class Graph {
    private Collection<Node> nodes;
    private Collection<Edge> edges;
    private Map<String, String> attributes;

    public Graph() {
        this.nodes = new ArrayList<>();
        this.edges = new ArrayList<>();
        this.attributes = new HashMap<>();
    }

    public Collection<Node> getNodes() {
        return this.nodes;
    }

    public Collection<Edge> getEdges() {
        return this.edges;
    }

    public Map<String, String> getAttributes() {
        return this.attributes;
    }
    
    public Graph(Map<String, String> attributes) {
        this.nodes = new ArrayList<>();
        this.edges = new ArrayList<>();
        this.attributes = new HashMap<>(attributes);
    }

    public Graph node(String name) {
        this.nodes.add(new Node(name, Collections.emptyMap()));
        return this;
    }

    public Graph node(String name, Map<String, String> attributes) {
        this.nodes.add(new Node(name, attributes));
        return this;
    }

    public Graph edge(String start, String end) {
        this.edges.add(new Edge(start, end));
        return this;
    }

    public Graph edge(String start, String end, Map<String, String> attributes) {
        this.edges.add(new Edge(start, end, attributes));
        return this;
    }

}
