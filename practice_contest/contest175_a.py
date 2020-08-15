# -*- using:utf-8 -*-

if __name__ == "__main__":
  s = list(input())
  sum = 0
  for i in range(3):
    if s[i] == 'R':
      sum = 1
  if s[0] == 'R' and s[1] =='R':
    sum += 1
  if s[1] == 'R' and s[2] == 'R':
    sum += 1
  print(sum)
  
