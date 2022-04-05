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