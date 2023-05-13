N = int(input())

A = list(map(int, input().split())) 

B = []

for i in range(N-1):
  d = A[i+1] - A[i]
  B.append(A[i])
  if abs(d) == 1:
    continue
  elif d > 0:
    for k in range(d-1):
      B.append(A[i]+k+1)
  elif d < 0:
    for k in range(abs(d)-1):
      B.append(A[i]-k-1)

B.append(A[N-1])
print(*B)



# #%%
# s = 5
# g = 1

# for k in range(abs(g-s)-1):
#   print(s - k - 1)