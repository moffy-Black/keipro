# -*- using:utf-8 -*-

class main:
  def T(n, y):
    for i in range(n+1):
      for j in range(n - i + 1):
        if y == 10000 * i + 5000 * j + 1000 * (n-i-j):
            return(i, j, n-i-j)
            break
    return (-1,-1,-1)

if __name__ == "__main__":
  n, y = map(int, input().split())
  x, y, z = main.T(n, y)
  print(x,y,z)