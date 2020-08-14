# -*- using:utf-8 -*-

class main:
  def Max(array):
    Alice = 0
    Bob = 0
    for i in range(len(array)):
      if i % 2 == 0:
        Alice += max(array)
      else:
        Bob += max(array)
      array.remove(max(array))
    print(Alice-Bob)


if __name__ == "__main__":
  n = int(input())
  array = list(map(int,input().split()))
  main.Max(array)
  
#解説
#max(配列)で配列の最大値を取得できる。min()で最小値
#配列から特定の値を削除したいときには配列.remove(特定の値)
