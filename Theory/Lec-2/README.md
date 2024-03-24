# Searching algorithms 

### Trees
- Hierarchical structure with a single root node and branches extending downward.
- Used for representing hierarchical relationships, such as file systems and organizational charts.

### Graphs
- Collection of nodes connected by edges (links or arcs), with no hierarchical relationship.
- Used for representing arbitrary relationships, such as social networks and transportation networks.

### Tree Terminologies:

1. **Node:** A fundamental unit of a tree structure, containing data and links to its child nodes (if any) and possibly its parent node.
  
2. **Root:** The topmost node in a tree hierarchy, from which all other nodes descend. It has no parent.
  
3. **Leaf:** A node in a tree that has no child nodes; it resides at the bottom of the tree.
  
4. **Parent:** A node in a tree that has child nodes.
  
5. **Child:** Nodes directly connected to a parent node in a tree.
  
6. **Siblings:** Nodes that share the same parent node.
  
7. **Depth:** The length of the path from the root to a particular node. The root has a depth of 0.
  
8. **Height:** The length of the longest path from a node to a leaf. The height of a leaf node is 0.
  
### Graph Terminologies:

1. **Node (Vertex):** A fundamental unit of a graph, representing an entity or object. Nodes may contain data.
  
2. **Edge:** A connection between two nodes in a graph, indicating a relationship between them.
  
3. **Directed Edge:** An edge with a specific direction from one node to another.
  
4. **Undirected Edge:** An edge with no specific direction; it connects nodes bidirectionally.
  
5. **Adjacent Nodes:** Nodes connected by an edge.
  
6. **Path:** A sequence of nodes connected by edges, indicating a route from one node to another.
  
7. **Cycle:** A path that starts and ends at the same node, forming a closed loop.
  
8. **Degree:** The number of edges incident to a node. In directed graphs, there are separate in-degree and out-degree for each node.

## Informed Search vs Uninformed Search  

| Criteria           | Informed Search                                      | Uninformed Search                                |
|--------------------|------------------------------------------------------|--------------------------------------------------|
| **Information Used** | Utilizes domain-specific knowledge or heuristics.   | Makes decisions solely based on the structure of the search space. |
| **Strategy**         | Makes informed decisions guided by heuristics.       | Explores the search space blindly without additional information. |
| **Examples**         | A* search, Greedy Best-First search, IDA*.           | Breadth-first search (BFS), Depth-first search (DFS), Iterative deepening depth-first search (IDDFS). |
| **Efficiency**       | Generally more efficient, especially with accurate heuristics. | May be less efficient, particularly in large or complex search spaces. |

## Breadth First Search (BFS) vs Depth First Search (DFS)    

| Criteria           | Breadth First Search (BFS)                         | Depth First Search (DFS)                            |
|--------------------|----------------------------------------------------|-----------------------------------------------------|
| **Strategy**       | Explores all nodes at the current depth level before moving to the next level. | Explores as far as possible along each branch before backtracking. |
| **Search Order**   | Explores nodes level by level, starting from the root. | Explores nodes depth-wise, going as deep as possible before backtracking. |
| **Data Structure** | Uses a queue data structure to maintain the order of nodes to be visited. | Uses a stack data structure (or recursion) to maintain the order of nodes to be visited. |
| **Completeness**   | Completeness guaranteed if the tree is finite.    | Not guaranteed to find a solution if the tree/graph is infinite or has cycles. |
| **Optimality**     | Finds the shallowest goal node, ensuring optimality for unweighted graphs. | May not find the shortest path, as it may find a deeper goal node before a shallower one. |
| **Memory Usage**   | Requires more memory as it needs to store all nodes at the current level. | Requires less memory compared to BFS, as it only needs to store nodes along the current path. |


### Breadth First Search

```plaintext
function breadth_first_search;
begin
    open := [Start];
    closed := [ ];

    while open [ ] do
    begin
        remove leftmost state from open, call it X;
        if X is a goal then return SUCCESS
        else begin
            generate children of X;
            put X on closed;
            discard children of X if already on open or closed;
            put remaining children on right end of open
        end
    end

    return FAIL
end
```

![image](https://github.com/Rohail30/AI/assets/96627590/ca1c66fd-de4a-45df-8ba5-5f243d664bc2)

### Depth First Search Algorithm

```plaintext
begin
    open := [Start];
    closed := [];
    
    while open + [ ] do
    begin
        remove leftmost state from open, call it X;
        if X is a goal then return SUCCESS
        else begin
            generate children of X;
            put X on closed;
            discard children of X if already on open or closed;
            put remaining children on left end of open
        end
    end;
    
    return FAIL
end
```

![image](https://github.com/Rohail30/AI/assets/96627590/9894b6a2-10f8-4ef3-9664-07bdcf167a92)












