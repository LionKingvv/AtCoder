#上から順にlistを読み込んでlistに格納していく。
a = [input().split() for l in range(9)]
print(a)


for i in range(9):
  for j in range(9):
    if a[i][0][j] == '#':
