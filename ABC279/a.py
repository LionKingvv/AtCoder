S = input()

l = 0

for i in range(len(S)):
  if S[i] == 'v':
    l += 1
  elif S[i] == 'w':
    l += 2

print(l)