s = input()

f = -2
for i in range(len(s)):
  if s[i] == 'a':
    f = i

print(f+1)