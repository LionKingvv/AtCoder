a, b = map(int,input().split())

if b == 0:
  print('No')
  exit()

dic = {}
for i in range(a):
  dic[i+1] = []

for _ in range(b):
  v, w = map(int,input().split())
  dic[v].append(w)
  dic[w].append(v)

count = 0
for i in range(a):
  l = len(dic[i+1])
  count += l
  if l == 0 or l > 2:
    print('No')
    exit()

if count / 2 != a-1:
  print('No')
  exit()

print('Yes')