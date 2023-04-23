N, T = map(int,input().split())
A = list(map(int, input().split()))

sum = 0
for i in range(N):
  sum += A[i]

b = T // sum # 繰り返す数 int(T/sum)だとだめ
c = T % sum # 秒数

# if c == 0:
#   if b > 0:
#     print(N, A[N-1])
#     exit()
#   else:
#     print(1,0)
#     exit()

S = 0
for j in range(N):
  # if c == S + A[j]:
  #   print(j + 1, A[j])
  #   exit()
  if c < S + A[j]:
    print(j + 1, T - (b * sum + S))
    exit()
  else:
    S += A[j]