# -*- using:utf-8 -*-

class main:
  def function(n,k,p,c):
    max = 0
    l = []
    for i in range(n):
      for j in range(k):
        max += c[p[i]]
        l.append(max)
    print(l)



if __name__ == "__main__":
   n, k = map(int, input().split())
   p = list(map(int, input().split()))
   c = list(map(int, input().split()))
   main.function(n,k,p,c)