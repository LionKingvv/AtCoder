a, b = map(int,input().split())

s = [int(input()) for _ in range(a)]
t = [int(input()) for _ in range(b)]

count = 0
for i in range(a):
  if s[i] % 1000 in t:
    count += 1

print(count)