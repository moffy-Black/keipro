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

#解説
#itertools.combinationsを使用すると順列や組み合わせの表現が楽にできる
#combination(list,n)でlistからｎ個の数字を取り出して新しく配列を作成する
#配列の並び替えに関してはsortedを使用すると数字の昇順、降順に並び変えることができる。