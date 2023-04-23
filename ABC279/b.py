S = input()
T = input()

flag = 0

if S == T or S.find(T) != -1:
  print('Yes')
else:
  print('No')