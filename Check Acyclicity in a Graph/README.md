# Check Acyclicity of a Graph
Courtesy of Coursera and UCSD's Graph Algorithm Course
## Task
Check whether a given directed graph with 𝑛 vertices and 𝑚 edges contains a cycle.

## Input Format
A graph is given in the standard format.

## Constraints
1 ≤ 𝑛 ≤ $10^3$, 0 ≤ 𝑚 ≤ $10^3$.

## Output Format
Output 1 if the graph contains a cycle and 0 otherwise.

## Sample 1.
Input:
4 4
1 2
4 1
2 3
3 1 <br>
Output:
1
1 2
4 3 <br>
This graph contains a cycle: 3 → 1 → 2 → 3.
## Sample 2.
Input:
5 7
1 2
2 3
1 3
3 4
1 4
2 5
3 5 <br>
Output:
0
1 2
4 3 5 <br>
There is no cycle in this graph. This can be seen, for example, by noting that all edges in this graph
go from a vertex with a smaller number to a vertex with a larger number.
