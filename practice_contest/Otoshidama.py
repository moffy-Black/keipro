# -*- using:utf-8 -*-

class main:
  def T(n, y):
    array = []
    for i in range(n+1):
      i += 1
      for j in range(n+1):
        j += 1
        for z in range(n+1):
          z += 1
          array.append(i, j, z)
    return array

if __name__ == "__main__":
  n, y = map(int, input().split())
  array = main.T(n, y)
  print(array)