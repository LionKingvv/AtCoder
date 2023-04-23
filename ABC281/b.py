S = input()

import string
omoji = list(string.ascii_uppercase)
num = ['{}'.format(i) for i in range(0,10)]

if len(S) != 8:
  print('No')
  exit()

if (S[0] not in omoji) or (S[7] not in omoji):
  print('No')
  exit()

for i in range(1,7):
  if S[i] not in num:
    print('No')
    exit()

if int(S[1:7]) < 100000 or int(S[1:7]) > 999999:
  print('No')
  exit() 

print('Yes')