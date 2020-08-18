# -*- using:utf-8 -*-
class main:
  def judge(s):
    if s == '':
      print('YES')
    else:
      print('NO')

if __name__ == "__main__":
  s = input().replace("eraser", "").replace("erase", "").replace("dreamer", "").replace("dream", "")
  main.judge(s)

#解説
#.replace('置き換られる文字','置き換える文字')の文法を知っとく。
#今回は各文字列を''何もない状態に変換している。