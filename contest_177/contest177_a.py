# -*- using:utf-8 -*-

class main:
  def judge(d, x):
    if d <= x:
      print("Yes")
    else:
      print("No")

if __name__ == "__main__":
  d, t, s = map(int, input().split())
  dis = t * s
  main.judge(d,dis)
  