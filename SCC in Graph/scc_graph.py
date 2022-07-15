# Uses python3

import sys

sys.setrecursionlimit(200000)

def explore(v, adj, post, visited):
    if not visited[v]:
        visited[v] = True
        adj_list = adj[v]
        for i in adj_list:
            if not visited[i]:
                explore(i, adj, post, visited)
        post.append(v)

def dfs(n, adj, visited):
    post_order = list()
    for i in range(n):
        explore(i, adj, post_order, visited)
    return post_order


def number_of_strongly_connected_components(n, adj, adj_r):
    result = 0
    visited = [False for _ in range(n)]
    post_order = list(reversed(dfs(n, adj_r, visited)))
    visited = [False for _ in range(n)]
    for vertex in post_order:
        if not visited[vertex]:
            explore(vertex, adj, post_order, visited)
            result += 1
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    edges_reverse = list(zip(data[1:(2 * m):2], data[0:(2 * m):2]))
    adj = [[] for _ in range(n)]
    adj_reverse = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    for (a, b) in edges_reverse:
        adj_reverse[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(n, adj, adj_reverse))

# post = [(0,post_of_0),(1,post_of_1),...] with post in increasing order
