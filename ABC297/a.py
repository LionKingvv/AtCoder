N, D = map(int,input().split())
T = list(map(int, input().split())) 

flag = -1

for i in range(N-1):
  if T[i+1]-T[i] <= D:
    flag = T[i+1]
    print(flag)
    exit()

print(flag)