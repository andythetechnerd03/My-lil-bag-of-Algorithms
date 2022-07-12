# Uses python3

import sys


# traversal: traversal starting at vertex v must end at v
def traversal(target, v, adj, explored):
    explored[v] = True
    result = False
    adj_list = adj[v]
    for i in adj_list:
        if i == target:
            return True
        if explored[i] is True:
            continue
        explored[i] == True
        result = result or traversal(target, i, adj, explored)
    return result


def acyclic(adj, n):
    result = False
    for i in range(n):
        explored = [False for _ in range(n)]
        result = traversal(i, i, adj, explored)
        if result:
            return 1
    return 1 if result else 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj, n))
