# -*- using:utf-8 -*-

class main:
  def coin(a, b, c, x):
    sum = 0
    for i in range(a + 1):
      i += 1
      for j in range(b + 1):
        j += 1
        for z in range(c + 1):
          z += 1
          if x == 500 * (i - 1) + 100 * (j - 1) + 50 * (z - 1):
            sum += 1
    print(sum)
          
          
  
if __name__ == "__main__":
  array = [int(input()) for i in range(4)]
  main.coin(array[0], array[1], array[2], array[3])
  