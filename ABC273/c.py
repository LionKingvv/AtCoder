N = int(input())
A = list(map(int, input().split()))

for i in range(N):
  count = 0
  for j in range(N):
    if A[i] < A[j]:
      count += 1
  
  print(count)