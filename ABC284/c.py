N, M = map(int,input().split())

if M == 0:
  print(N)
  exit()

dic = {}
for i in range(N):
  dic[i+1] = []

for _ in range(M):
  v, w = map(int,input().split())
  dic[v].append(w)
  dic[w].append(v)

print(dic)

l = {}
for i in range(N):
  l[i] = 0

for i in range(N):
  l[len(dic[i+1])] += 1

count = 0
for i in range(N):
  if l[i] != 0:
    count += 1

print(count)