import itertools

N, M = map(int,input().split())

ans = set([i+1 for i in range(N)])

a = [None]*M
alist = [None]*M

for i in range(M):
  _ = int(input())
  a[i] = list(map(int, input().split()))
  alist[i] = int("".join(map(str, a[i])))

count = 0
print (alist)
for i in range(M):
  all = list(itertools.combinations(alist,i+1))
  for l in all:
    h = []
    for ll in l:
      ll = [int(a) for a in str(ll)]
      print(ll)
      h.append(ll)
    print(h)
    h = set(h)
    print(h)
    if ll == ans:
      count += 1

print(count)