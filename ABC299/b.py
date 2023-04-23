N, T = map(int,input().split())
C = list(map(int, input().split())) 
R = list(map(int, input().split())) 

col0 = C[0]
max0 = R[0]
p0 = 0

col = 0
max = 0
p = 0

for i in range(N):
    if C[i] == T and R[i] > max:
        max = R[i]
        p = i
    if C[i] == C[0] and R[i] > max0:
        max0 = R[i]
        p0 = i

if max != 0:
    print(p+1)
else:
    print(p0+1)