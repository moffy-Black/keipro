# -*- using:utf-8 -*-

class main:  
  def input(n, t, x, y):
    flag = 'Yes'
    for i in range(n):
      li = list(map(int, input().split()))
      t.append(li[0])
      x.append(li[1])
      y.append(li[2])
      if abs((x[i+1] -x[i]) + (y[i+1] - y[i])) > t[i+1] - t[i] or (x[i+1] + y[i+1] - t[i+1])%2 != 0:
        flag = 'No'
    print(flag)

    
if __name__ == "__main__":
  n = int(input())
  t = [0]
  x = [0]
  y = [0]
  main.input(n, t, x, y)