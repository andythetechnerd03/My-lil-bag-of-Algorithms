# Uses python3

import sys
import queue
import math
import heapq


def distance(n, adj, cost, s, t):
    # write your code here
    dist_values = [math.inf for _ in range(n)]
    dist_values[s] = 0
    finished = [False for _ in range(n)]
    heap = [[0, s]]
    heapq.heapify(heap)
    while len(heap) != 0:
        u = heapq.heappop(heap)
        finished[u[1]] = True
        adj_list = adj[u[1]]
        for v in range(len(adj_list)):
            if finished[adj_list[v]] is False:
                if dist_values[u[1]] + cost[u[1]][v] < dist_values[adj_list[v]]:
                    dist_values[adj_list[v]] = dist_values[u[1]] + cost[u[1]][v]
                    heapq.heappush(heap, [dist_values[adj_list[v]], adj_list[v]])
    return dist_values[t]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    answer = distance(n, adj, cost, s, t)
    print(answer if answer != math.inf else -1)
