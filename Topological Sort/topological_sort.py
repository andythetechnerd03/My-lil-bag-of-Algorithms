# Uses python3

import sys


def dfs(adj, used, order, x):
    adj_list = adj[x]
    if not adj_list:
        order.append(x)
        return
    for v in adj_list:
        if used[v]:
            continue
        used[v] = True
        dfs(adj, used, order, v)
    order.append(x)
    pass


def toposort(n, adj):
    used = [False for _ in range(n)]
    order = []
    for i in range(n):
        if not used[i]:
            used[i] = True
            dfs(adj, used, order, i)
    return order


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = reversed(toposort(n, adj))
    for x in order:
        print(x + 1, end=' ')
