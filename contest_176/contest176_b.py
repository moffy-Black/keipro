# -*- using:utf-8 -*-

# class main:

if __name__ == "__main__":
  n = int(input())
  s = sum(list(map(int, str(n))))
  if s % 9 == 0:
    print('Yes')
  else:
    print('No')