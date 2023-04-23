#%%
import numpy as np
from functools import lru_cache

@lru_cache(maxsize=1000)
def calc(k):
  if k == 0:
    return 1
  else:
    return calc(np.floor(k/2)) + calc(np.floor(k/3))

N = int(input())

print(calc(N))
