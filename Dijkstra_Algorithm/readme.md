# Dijkstra-shortest-path
Implementation of Dijkstra's algorithm to find the shortest path from S (starting node) to all the other nodes in a graph. 

The input to program should be a text file which is the adjacency Matrix for the graph.
For example for the below graph : 

<img width="372" alt="screen shot 2017-05-25 at 10 59 57 pm" src="https://cloud.githubusercontent.com/assets/23372809/26478960/f9ebd3ce-419d-11e7-9678-58e05c9d40d6.png">

The adjacency matrix is (-99 represent no edge):

0,5,-99,10,15

-99,0,1,4,-99

-99,-99,0,2,-99

-99,3,-99,0,-99

-99,-99,8,-99,0




## Instructions to execute:
1. make
2. ./Q2_dijikstra.out {input-file}
  example: ./Q2_dijikstra.out matrix_org.txt
3. make clean
