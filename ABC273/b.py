#%%
X, K = map(int, input().split())

for i in range(1,K+1):
  X = round(X,-i)

print(X)

#%%
# 参考元: https://note.nkmk.me/python-round-decimal-quantize/
def my_round(val, digit=0):
    p = 10 ** digit
    return (val * p * 2 + 1) // 2 / p

X, K = map(int, input().split())

for i in range(1,K+1):
  X = my_round(X,-i)

print(int(X))

#%%
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
X, K = map(int, input().split())

for i in range(1,K+1):
  X = int(Decimal(X).quantize(Decimal('1E{}'.format(i)), rounding=ROUND_HALF_UP))
  
print(X)