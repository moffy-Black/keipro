# -*- using:utf-8 -*-
class main:

  def seki(a, b):
    s = a * b
    return s
  
  def judge(s):
    if s % 2 == 0:
      print('Even')
    else:
      print('Odd')

if __name__ == "__main__":
  a, b = map(int, input().split())
  s = main.seki(a, b)
  main.judge(s)
  