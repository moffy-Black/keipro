# -*- using:utf-8 -*-
from itertools import combinations

class main:
  def T(array):
    cnt = 0
    for i in array:
      a, b, c = i
      if a != b and a != c and b != c and a < b + c:
        cnt += 1
    print(cnt)

  def Sort(array):
    for i in range(len(array)):
      array[i] = sorted(array[i], reverse=True)
    return array

if __name__ == "__main__":
  n = int(input())
  l = list(map(int, input().split()))
  array = list(combinations(l, 3))
  array = main.Sort(array)
  main.T(array)
      