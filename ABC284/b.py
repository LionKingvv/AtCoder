N = int(input()) #1行目のNを取得する

for _ in range(N):
  t = int(input())
  que = list(map(int, input().split()))
  count = 0
  for i in range(t):
    if que[i] % 2 == 1:
      count += 1
  
  print(count)