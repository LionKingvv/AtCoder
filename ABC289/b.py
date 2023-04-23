from collections import deque

N, M = map(int,input().split())
a = list(map(int, input().split())) # レ点の位置

l = deque()

# 1:1, 2:3, 3:4
# a = [1,0,1,1,0] # レ点の位置

deq = deque()
for i in range(1, N+1):
  if i in a:
    deq.append(i)
  else:
    l.append(i)
    while(deq):
      l.append(deq.pop())
    deq = deque()

while(deq):
  l.append(deq.pop())
print(*l)

# 1 レ 2 3 レ 4 レ 5

# deq ← 1
# deq = [1]
# l ← 2
# l ← pop(deq)
# l = [2,1]
# deq ← 3,4
# l ← 5
# l ← pop(deq)
# l = [2,1,5,4,3]