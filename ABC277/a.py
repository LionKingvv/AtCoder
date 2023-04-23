N, M = map(int,input().split())
P = list(map(int, input().split()))

for i in range(N):
  if P[i] == M:
    print(i+1)