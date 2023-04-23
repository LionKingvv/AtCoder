import itertools

N, K, D = map(int,input().split())
A = list(map(int, input().split()))

s = set() 

for balls in itertools.combinations(A, K):
  s.add(sum(list(balls)))

max = -1
for i in s:
  if i % D == 0:
    if max < i:
      max = i

print(max)