S = list(input())
alf = [chr(ord("a")+i) for i in range(26)]
 
i = 0
l = len(S)
box = {}
b = [0 for _ in range(l)]
 
for k in range(26):
  box[chr(ord("a")+k)] = 0
 
 
while(i < l):
  s = S[i]
  if s == '(':
    i += 1
    continue
  elif s in alf:
    if box[s] > 0:
      print('No')
      exit()
    else:
      box[s] += 1
      b[i] += 1
  elif s == ')':
    j = i-1
    while(j >= 0):
      if S[j] == '(':
        for k in range(j, i):
          if b[k] > 0:
            box[S[k]] = 0
        S[j] = '0'
        j = 0
      j -= 1
  i += 1
 
print('Yes')
