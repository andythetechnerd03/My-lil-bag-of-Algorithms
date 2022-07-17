# Uses python3

import sys
import queue


def distance(n, adj, s, t):
    # utilize the queue data structure to handle this problem
    distances = [-1 for _ in range(n)]
    distances[s] = 0
    q = [s]
    lenq = 1
    # Basically we go through all node and attach the distance = distance of previous node + 1 to it
    while len(q) != 0:
        dequeue = q.pop(0)
        lenq -= 1
        adj_list = adj[dequeue]
        d = distances[dequeue]
        for node in adj_list:
            if distances[node] == -1:
                q.append(node)
                lenq += 1
                distances[node] = d + 1

    return distances[t]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(n, adj, s, t))
