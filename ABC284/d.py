T = int(input())

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

for _ in range(T):
  n = int(input())
  f = factorization(n)

  # print(f)
  c = [0, 0]
  for i in range(2):
    if f[i][1]-1 == 0:
      c[1] = f[i][0]
    else:
      c[0] = f[i][0]
  print(*c)