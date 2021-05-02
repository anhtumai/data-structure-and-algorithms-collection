# Graph search

Generic alogirthm:

- BFS: breadth first search
- DFS: depth first search

Pseudo pseudo codes:

- initially s explored, all other vertices unexplored
- while possible:
  - choose an edge (u,v) with u explored and v unexplored
  - mark v explored

## BFS

Data structure in use: queue(FIFO)

Pseudo pseudo code:

- initial, start node s
- mark s as explored
- let Q = queue data structure (FIFO), initialized with s
- while Q not empty:
  - remove the first node of Q, call it v
  - for each edge (v,w):
        - if w unexplored:
            - mark w as explored
            - add w to Q (at the end)

## DFS

Aggressively traverse through a graph. When hit a dead end, or all neighbors are visited node, backtrack.

Do not guarantee to provide a shortes path.

- Add starting node to visited
- Check all neighbour node
- If neighbour node is not visited, call this subroutine again on this node

## Topological sort

Applied for Directed Acyclic Graph (DAG)

Linear ordering of vertices such that for every directed edge u v, vertex u comes bedore v in the ordering

This can be done with modification of DFS:

- check a node, traverse through it the same way as DFS

- if a node doesn't lead to anywhere, or only lead to visited node, add that to the stack

- do it untill all node are in the stack

- print the content of the stack in reverse order

## Computing SCC (Strongly connected components)

### Kosajary's two-pass algorithm

- G(rev) = G with all arcs reversed
- run DFS-Loop on G(rev): ordering the ordering of nodes
- run DFS-Loop on G: disconvering SCC one by one

Idea: if there are SCCs, they have the same leaders in both G and G(rev)


## Weighted graph

How to reprensent a weighted graph

- Adjacency matrix representation:

```txt
0 ∞ 6 3 ∞
3	0	∞	∞	∞
∞	∞	0	2	∞
∞	1	1	0	∞
∞	4	∞	2	0
```

- Adjacency list representation:

```python3
[1,[3,6],[4,3]],
[2,[1,3]],
[3,[4,2]],
[4,[2,1],[3,1]]
```

## Djikstra algorthim shortest path

Initiailize:

- Let distance of start vertext from start vertext = 0
- Other distance is Inf

While (unvisited is not empty):

- Visit the unvisited with the smallest known distance from the start
- For the current vertext, examine its unvisited neighbours
- If the calculated distance < known distance, update the shortest distance
- Update the previous vertex for each of the updated distances
- Add current vertex to the list of visited vertices
