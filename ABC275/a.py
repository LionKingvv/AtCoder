N = int(input())
A = list(map(int, input().split()))

# maxとlist.indexによる実装
max_value = max(A)
max_index = A.index(max_value)
print(max_index+1)
