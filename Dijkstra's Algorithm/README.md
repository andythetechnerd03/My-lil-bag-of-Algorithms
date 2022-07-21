# Computing the Minimum Cost of a Flight
## Problem Introduction
You wanna go home early, right? Use Dijkstra right now! (Text Courtesy of UCSD of Coursera)
## Problem Description
### Task
Given an directed graph with positive edge weights and with 𝑛 vertices and 𝑚 edges as well as two
vertices 𝑢 and 𝑣, compute the weight of a shortest path between 𝑢 and 𝑣 (that is, the minimum total
weight of a path from 𝑢 to 𝑣).
### Input Format
A graph is given in the standard format. The next line contains two vertices 𝑢 and 𝑣.
Constraints. 1 ≤ 𝑛 ≤ 104, 0 ≤ 𝑚 ≤ 105, 𝑢 ̸= 𝑣, 1 ≤ 𝑢, 𝑣 ≤ 𝑛, edge weights are non-negative integers not
exceeding 108.
### Output Format
Output the minimum weight of a path from 𝑢 to 𝑣, or −1 if there is no path.
## Sample 1
### Input:
4 4 <br>
1 2 1 <br>
4 1 2 <br>
2 3 2 <br>
1 3 5 <br>
1 3 <br>
### Output:
3 <br>
There is a unique shortest path from vertex 1 to vertex 3 in this graph (1 → 2 → 3), and it has weight 3.
## Sample 2
### Input:
5 9 <br>
1 2 4 <br>
1 3 2 <br>
2 3 2 <br>
3 2 1 <br>
2 4 2 <br>
3 5 4 <br>
5 4 1 <br>
2 5 3 <br>
3 4 4 <br>
1 5 <br>
### Output:
6 <br>
There are two paths from 1 to 5 of total weight 6: 1 → 3 → 5 and 1 → 3 → 2 → 5.
## Sample 3.
### Input:
3 3 <br>
1 2 7 <br>
1 3 5 <br>
2 3 2 <br>
3 2 <br>
### Output:
-1 <br>
There is no path from 3 to 2.

## Tips
Use binary heap :))
