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
