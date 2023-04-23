import copy

N = int(input())
P = list(map(int, input().split()))
print(P)
def swap(l,a,b):
  tmp = l[a]
  l[a] = l[b]
  l[b] = tmp
  return l

P_sort = sorted(P)
print(P_sort)
count = 1
flag = 0
r = N
l = N-1
P_c=copy.copy(P_sort)
while flag == 1:
  if l == 0:
    r -= 1
    l = r-1

  P_c = swap(P_c)

  if P_c == P:
    flag = 1
    P_c[l],P_c[r] = P_c[r],P_c[l]
  else:
    l -= 1

print(P_c)