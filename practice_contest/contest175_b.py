# -*- using:utf-8 -*-

class main:
  def T(array):
    s = 0
    for i in range(len(array)):
      i += 1
      for j in range(len(array) - (i - 1)):
        print(array[j], array[j + 1], array[j + 2])
        
if __name__ == "__main__":
  n = int(input())
  l = list(map(int, input().split()))
  array = list(set(l))
  main.T(array)
      