# -*- using:utf-8 -*-

class main:
  def function(n, a):
    mod = 10 **9 +7
    S = [0] * (n + 1)
    for i in range(n):
      S[i + 1] = S[i] + a[i]
    SN = S[-1]
    ans = 0
    for i in range(n - 1):
      cnt = a[i] * (SN - S[i + 1])
      ans += cnt
    print(ans % mod)



if __name__ == "__main__":
  n = int(input())
  a = list(map(int, input().split()))
  main.function(n,a)



# self------------------------------------
# from itertools import combinations

# class main:
#   def v(array):
#     sum = 0
#     for i in range(len(array)):
#       sum += array[i][0] * array[i][1]
#     sum = sum % 1000000007
#     print(sum)

# if __name__ == "__main__":
#   n = int(input())
#   a = list(map(int, input().split()))
#   array = list(combinations(li, 2))
#   main.v(array)