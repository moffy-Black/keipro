# -*- using:utf-8 -*-

class main:
  def count(c,array):
    while all(i % 2 == 0 for i in array):
      array = [j/2 for j in array]
      c += 1
    return c

if __name__ == "__main__":
  n = int(input())
  array = list(map(int, input().split()))
  c = 0
  c = main.count(c, array)
  if c is None:
    print(0)
  print(c)

# 解説
# all(条件式 for 変数 in 配列名)で配列の要素が全て条件式に一致していればTrueを返す。
# while:
#   return
#   ではなく
# while
# return