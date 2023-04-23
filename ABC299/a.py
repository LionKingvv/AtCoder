N = int(input())
S = input()

count = 0

for i in range(N):
    if S[i] == '|':
        count += 1
    if S[i] == '*':
        if count == 1:
            print('in')
        else:
            print('out')
        exit()