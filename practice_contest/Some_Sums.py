# -*- using:utf-8 -*-

class main:
  def get_list(n):
    li = []
    for i in range(n):
      li.append(i + 1)
    return li

  def sum_digit(n):
    sum = 0
    while n > 0:
      sum += n % 10
      n = n // 10
    return sum

  def judge(li_1, li_2, a, b):
    sum = 0
    for i in range(len(li_1)):
      if a <= li_2[i] and li_2[i] <= b:
        sum += li_1[i]
    print(sum)


if __name__ == "__main__":
  array = list(map(int,input().split()))
  li_1 = main.get_list(array[0])
  li_2 = []
  for i in range(array[0]):
    li_2.append(main.sum_digit(li_1[i]))
  main.judge(li_1, li_2, array[1], array[2])
  
#解説
#list(map(int,input().split()))のカッコに注意
#各桁の値を取得するには　n % 10で余りを出せばいい。
# // は切り捨て除算