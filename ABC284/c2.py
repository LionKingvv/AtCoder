import numpy as np
from scipy.sparse.csgraph import connected_components

n, m = map(int, input().split())
graph = [[0]*n for _ in range(n)]

if m == 0:
  print(n)
  exit()

for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1  # 有向グラフなら消す

a = np.array(graph)
n, labels = connected_components(a)
print(n)