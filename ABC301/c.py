alp = [chr(i) for i in range(97, 97+26)]

def Counter(string):
    counter = {}
    for k in alp:
        counter[k] = 0
    counter['@'] = 0
    for c in string:
        counter[c] += 1
    return(counter)

at = ['a', 't', 'c', 'o', 'd', 'e', 'r']
not_at = [i for i in alp if i not in at]

# S = list(input())
# T = list(input())
S = Counter(input())
T = Counter(input())

if S == T:
    print('Yes')
    exit()

for k in not_at:
    if S[k] != T[k]:
        print('No')
        exit()

sc = 0
tc = 0

sas = 0
sat = 0

for k in at:
    sa = S[k] - T[k]
    if sa > 0:
      sas += sa
    else:
      sat += sa

# for k in at:
#     sc += S[k]
#     tc += T[k]
# if (sc + S['@']) == (tc + T['@']):
#     print('Yes')
#     exit()

if (sas + S['@']) == (sat + T['@']):
    print('Yes')
    exit()


print('No')
