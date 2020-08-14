# -*- using:utf-8 -*-


if __name__ == "__main__":
  n = int(input())
  array = [int(input()) for i in range(n)]
  print(len(set(array)))

#解説
#n個の複数行に数値を入力する場合、リスト = [int(input()) for i in range(n)]で取得する。
#list型をset型に直すと配列の要素の重複をなくせる。