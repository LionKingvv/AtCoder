A = list(map(int, input().split()))

num = A[0]*A[1]*A[2] - A[3]*A[4]*A[5]

print(num%998244353)