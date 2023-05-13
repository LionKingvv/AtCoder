
N = int(input())
S = input()

t = 0
a = 0

if N % 2 == 0:
    w = N / 2
else:
    w = int(N / 2) + 1

for s in S:
    if s == 'T':
        t += 1
    else:
        a += 1
    
    if t == w or a == w:
        break

if t >= a:
    print('T')
else:
    print('A')