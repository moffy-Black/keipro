# -*- using:utf-8 -*-

def jou(x, y):
  ans = x * y
  return ans

if __name__ == "__main__":
  li = list(map(int, input().split()))
  array = []
  array.append(li[0] * li[2])
  array.append(li[0] * li[3])
  array.append(li[1] * li[2])
  array.append(li[1] * li[3])
  
  print(max(array))
