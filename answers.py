#4
n = str(input()).split(' ')
a = 1
for i in n:
  a *= int(i)
print(a)

#5
import math

l = input()
s = 0
for i in str(input()).split(' '):
  s += int(i)

print(s % 100)

#6
print(2*int(input())+3)

#7
test_line = input().split(' ')
total = 0
for i in range(1, int(test_line[0])+1):
  if i % int(test_line[1]) == 0:
    total += 1
    continue
  elif i % int(test_line[2]) == 0:
    total += 1
print(total)

#8
input_line = input().split(' ')
total = 0
for i in range(1, int(input_line[0])+1):
  for j in range(1, int(input_line[0])+1):
    if (i + j) <= int(input_line[1]):
      total += 1
print(total)

#9

#10
total = 1
for i in range(1, int(input())+1):
  total *= i
print(total)

#11
import math

for i in range(2, int(input())+1):
  for j in range(2, i):
    if i % j == 0:
      break
  # breakしなかった（iがjで一度も割り切れなかった(＝素数)とき出力）
  else:
    print(i, end=' ')