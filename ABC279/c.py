M, N = map(int, input().split())
S = [list(input()) for _ in range(M)]
T = [list(input()) for _ in range(M)]

H = [[None for _ in range(M)] for j in range(N)]
for i in range(N):
  for j in range(M):
    print(i,j)
    H[i][j] = S[j][i]
    print(H[i][j])
    

print(S)
print(H)