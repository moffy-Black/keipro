# -*- using:utf-8 -*-

def factorial_cor(n):
  fact = 1
  for integer in range(1, n + 1):
    fact *= integer
  return fact

if __name__ == "__main__":
  MOD = 1000000007
  N = int(input())
  if N == 1:
    print(0) 
  else:
    C = factorial_cor(N)
    ans = C * 10**(N-2) % MOD
    print(int(ans))

