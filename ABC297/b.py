S = input()

x = -1
y = -1

for i in range(8):
  if S[i] == 'B' and x < 0:
    x = i
  elif S[i] == 'B':
    y = i

if (x+y) % 2 == 0:
  print('No')
  exit()

x = -1
y = -1
z = -1

for i in range(8):
  if S[i] == 'R' and x < 0:
    x = i
  elif S[i] == 'R':
    y = i
  elif S[i] == 'K':
    z = i

if x < z and z < y:
  print('Yes')
  exit()

print('No')