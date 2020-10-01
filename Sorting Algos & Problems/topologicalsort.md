# Topological Sort

Topological sort of a directed acyclic graph [DAG] is partial ordering of its nodes such that U < V implies there must not exist a path from V to U.


Kahn’s algorithm I implemented, instead produces a linear ordering such that […, U, …, V, …] means there may be a path from U to V, but not vice versa.

<br>

<p align='center'>
  <img  src="https://miro.medium.com/max/750/1*eBCiN-5s9NKB55Rj3qJweA.png" alt="Algorithm graphics" width="500" height="300">
</p>

Partial ordering is very useful in many situations. One of them arises in parallel computing where a program can be represented as DAG.

```
E = (A + B) * (C - D)
```
Each node represents an operation and directed links in between are their dependencies.

<br>

<p align='center'>
  <img  src="https://miro.medium.com/max/713/1*Ls1TE93OCACX0pjbuV4FdQ.png" alt="Algorithm graphics" width="500" height="300">
</p>

<br>

There are 8 operations [including fetch and store] in this expression, but modern super-scalar CPUs are able to execute some operations in parallel to reduce the execution time up to 4 steps.

## How does this works?

We have already discussed about the relationship between all four types of edges in the DFS. Below is the relation we have seen between the departure time for different types of edges involved in a DFS of directed graph-

```
Tree edge (u, v): departure[u] > departure[v]
Back edge (u, v): departure[u] < departure[v]
Forward edge (u, v): departure[u] > departure[v]
Cross edge (u, v): departure[u] > departure[v]
```

As we can see that for a tree edge, forward edge or cross edge <font face="consolas" size="3">(u, v), departure[u]</font> is more than <font face="consolas" size="3">departure[v]</font>. But only for back edge the relationship <font face="consolas" size="3">departure[u] &lt; departure[v]</font> is true. So it is guaranteed that if an edge <font face="consolas" size="3">(u, v)</font> has <font face="consolas" size="3">departure[u] &gt; departure[v]</font>, it is not a back-edge.</p>
<p> <br>
We know that <strong>in DAG no back-edge is present</strong>. So if we order the vertices in order of their decreasing departure time, we will get topological order of graph (<strong>every edge going from left to right</strong>).</p>

<br>

<p align='center'>
  <img  src="https://www.techiedelight.com/wp-content/uploads/2016/11/Edges-Showing-Depature-Time.png" alt="Algorithm graphics" width="500" height="300">
</p>