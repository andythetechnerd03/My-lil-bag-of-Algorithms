# Minimum number of edges to go from 1 node to another
Courtesy of UCSD and Coursera for the problem.
## Problem Introduction
You would like to compute the minimum number of flight segments to get from one city to another one. For
this, you construct the following undirected graph: vertices represent cities, there is an edge between two
vertices whenever there is a flight between the corresponding two cities. Then, it suffices to find a shortest
path from one of the given cities to the other one.
## Problem Description
### Task
Given an undirected graph with π vertices and π edges and two vertices π’ and π£, compute the length
of a shortest path between π’ and π£ (that is, the minimum number of edges in a path from π’ to π£).
### Input Format
A graph is given in the standard format. The next line contains two vertices π’ and π£.
### Constraints
2 β€ π β€ 105, 0 β€ π β€ 105, π’ ΜΈ= π£, 1 β€ π’, π£ β€ π.
### Output Format
Output the minimum number of edges in a path from π’ to π£, or β1 if there is no path.

## Sample 1.
### Input:
4 4 <br>
1 2 <br>
4 1 <br>
2 3 <br>
3 1 <br>
2 4 <br>
### Output:
2 <br>
There is a unique shortest path between vertices 2 and 4 in this graph: 2 β 1 β 4.
## Sample 2.
### Input:
5 4 <br>
5 2 <br>
1 3 <br>
3 4 <br>
1 4 <br>
3 5 <br>
### Output:
-1 <br>
There is no path between vertices 3 and 5 in this graph.
