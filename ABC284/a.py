N = int(input()) #1行目のNを取得する
s = [input() for _ in range(N)] #複数行の数値の入力を取得

for i in range(N-1,-1,-1):
  print(s[i])