# -*- using:utf-8 -*-

# class main:

if __name__ == "__main__":
  n = int(input())
  ai = list(map(int, input().split()))
  li = []
  for i in range(n - 1):
    if ai[i] > ai[i + 1]:
      li.append(ai[i] - ai[i + 1])
      ai[i+1]=ai[i]
    else:
      pass
  print(sum(li))
