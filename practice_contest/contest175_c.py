# -*- using:utf-8 -*-

if __name__ == "__main__":
  li = list(map(int, input().split()))
  s = li[0]
  for i in range(li[1]):
    if s >= li[2]:
      s = s - li[2]
    else:
      s = s + li[2]
  print(abs(s))