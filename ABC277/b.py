N = int(input())
P = [input() for l in range(N)]

l1 = ['H' , 'D' , 'C' , 'S']
l2 = ['A' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , 'T' , 'J' , 'Q' , 'K']

f = 1

for i in range(N):
  if f == 1:
    for j in range(N-1, i, -1):
      if P[i] == P[j]:
        print('No')
        f = 0
        break

if f == 1:
  for i in range(N):
    if P[i][0] not in l1 or P[i][1] not in l2:
      print('No')
      f = 0
      break

if f == 1:
  print('Yes')