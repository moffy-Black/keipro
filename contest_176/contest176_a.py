# -*- using:utf-8 -*-

class main:
  def judge(n, x, t, s):
    if n % x > 0:
      print((s + 1) * t)
    else:
      print(s*t)

if __name__ == "__main__":
  n, x, t = map(int, input().split())
  s = n // x
  main.judge(n,x,t,s)