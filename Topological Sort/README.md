# Determining an Order of Courses

## Problem Introduction
Now, when you are sure that there are no cyclic dependencies in the given CS curriculum, you would like to
find an order of all courses that is consistent with all dependencies. For this, you find a topological ordering
of the corresponding directed graph.

## Problem Description
### Task
Compute a topological ordering of a given directed acyclic graph (DAG) with 𝑛 vertices and 𝑚 edges.

### Input Format
A graph is given in the standard format.

### Constraints
1 ≤ 𝑛 ≤ 105, 0 ≤ 𝑚 ≤ 105. The given graph is guaranteed to be acyclic.

### Output Format
Output any topological ordering of its vertices. (Many DAGs have more than just one
topological ordering. You may output any of them.)

## Sample 1.
Input: <br>
4 3 <br>
1 2 <br>
4 1 <br>
3 1 <br>
Output: <br>
4 3 1 2 <br>

## Sample 2
Input: <br>
4 1 <br>
3 1 <br>
Output: <br>
2 3 1 4 <br>

## Sample 3
Input: <br>
5 7 <br>
2 1 <br>
3 2 <br>
3 1 <br>
4 3 <br>
4 1 <br>
5 2 <br>
5 3 <br>
Output: <br>
5 4 3 2 1

## Tips
I recommend you take a look at this visualization at https://www.cs.usfca.edu/~galles/visualization/TopoSortDFS.html
to get an idea of how to do this algorithm
