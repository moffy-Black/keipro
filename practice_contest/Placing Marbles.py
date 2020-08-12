# -*- using:utf-8 -*-

class main:
  def count(n):
    print(n.count("1"))

# function place
if __name__ == "__main__":
  n = input()
  main.count(n)
# to do place

# 解説  
# str型でinputを受け取る。
# strから "1" を探してその数をカウントする。
# .countを知っているかどうかが大切。