S = input()
N = int(input())

bn = int(format(N, 'b'))
l = len(format(N, 'b'))

if len(S) < l:
  S.replace('?','1')
  print(S.replace('?','1'))
# elif len(S) == l:
  # while True:
    # max = 
    # if 