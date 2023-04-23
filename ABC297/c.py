H, W = map(int, input().split())
S = []
for i in range(H):
  S.append(list(input().strip()))

while 1:
  flag = -1
  for i in range(H):
    for j in range(W-1):
      if S[i][j] == S[i][j+1] == 'T':
        S[i][j] = 'P'
        S[i][j+1] = 'C'
        flag = 1
  if flag == -1:
    break

for i in range(H):
  print(''.join(S[i]))