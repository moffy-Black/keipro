# -*- using:utf-8 -*-
from itertools import combinations

if __name__ == "__main__":
  n = int(input())
  li = list(map(int, input().split()))
  array = list(combinations(li, 2))
  sum = 0
  mod = 1000000007
  for i in range(n):
    sum += array[i][0] * array[i][1]
  ans = sum % mod
  print(ans)