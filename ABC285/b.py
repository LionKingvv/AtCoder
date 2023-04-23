N = int(input())
S = input()


for l in range(N-1):
  l += 1
  max = 0
  i = 0
  while(i + l < N):
    # print('i = {}, l = {}'.format(i,l))
    if S[i] != S[i+l]:
      max = i + 1
    else:
      break
    i += 1
  print(max)