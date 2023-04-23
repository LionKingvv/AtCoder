N, M = map(int,input().split())
dict = {}

for i in range(N):
  dict[i+1] = []
# dict = {i+1: [] for i in range(N)} #これ1行で大丈夫

for i in range(M):
  A, B = map(int, input().split())
  dict[A].append(B)
  dict[B].append(A)
  # dequeを使って末尾に追加した方がいいです

for i in range(N):
  dict[i+1].sort()

for i in range(M):
  l = len(dict[i+1])
  if l != 0:
    L = [str(a) for a in dict[i+1]]
    L = " ".join(L)
    print(l,L)

    # print(l, *dict[i+1]) # アスタリスクでリストの要素を空白で表示できる
  else:
    print(0)