# -*- using:utf-8 -*-

class main:
  def function(s):
    if s % 9 == 0:
      print('Yes')
    else:
      print('No')

if __name__ == "__main__":
  n = int(input())
  s = sum(list(map(int, str(n))))
  main.function(s)