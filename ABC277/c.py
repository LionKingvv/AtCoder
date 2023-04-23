# 参考: https://atcoder.jp/contests/abc277/submissions/36452252

from collections import defaultdict, deque
n = int(input())

graph = defaultdict(list)
for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

que = deque()
que.append(1)
s = {1}

while que:
    v = que.popleft()
    for i in graph[v]:
        if not i in s:
            que.append(i)
            s.add(i)

print(max(s))