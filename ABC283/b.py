N = int(input())
A = list(map(int, input().split()))
Q = int(input())

for _ in range(Q):
  que = list(map(int, input().split()))

  if que[0] == 1:
    A[que[1]-1] = que[2]
  else:
    print(A[que[1]-1])