# -*- using:utf-8 -*-

# class main:

if __name__ == "__main__":
  h, w, m = map(int, input().split())
  li = []
  height = []
  width = []
  count_h = []
  count_w = []
  for i in range(m):
    li.append(input().split())
    height.append(li[i][0])
    width.append(li[i][1])

  for j in range(m):
    count_h.append(height.count(str(j+1)))
    count_w.append(width.count(str(j+1)))
  print(max(count_h)+max(count_w))