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

#12
import math

def judge():
  target = int(input())
  for i in range(2, math.floor((target+1)**0.5)):
    if target % i == 0:
      print('No')
      return
  print('Yes')
judge()

#13
import math

def judge():
  target = int(input())
  for i in range(1, math.floor((target)**0.5)+1):
    if target % i != 0:
      continue
    elif target % i == 0:
      print(i)
      print(math.floor(target / i))
judge()

#14
# 素因数分解
import math

def judge():
  target = int(input())
  result = []
  for i in range(2, math.floor((target)**0.5)+1):
    while True:
      if target % i == 0:
        result.append(i)
        target = target // i
      else:
        break
  if target > math.floor((target)**0.5):
    result.append(target)
  print(*result)
judge()

#15
# 最大公約数
import math

res = 0
def euclideanAlgo(a,b):
  global res
  if a > b:
    a = a % b
  elif b > a:
    b = b % a

  if a != 0 and b != 0:
    euclideanAlgo(a, b)
  elif a == 0:
    res = b
  elif b == 0:
    res = a

fir,sec = input().split(' ')
euclideanAlgo(int(fir),int(sec))
print(res)

#16
# ３つ以上の数の最大公約数
import math

def euclideanAlgo(a,b):
  if b == 0:
    return a

  s = a % b
  return euclideanAlgo(b, s)

calcIndex = 0
def commonDivisor(ary):
  global calcIndex
  res = 0

  for i in range(aryLength - 1):
    if i == 0:
      res = euclideanAlgo(ary[0], ary[1])
      calcIndex = 2
    else:
      res = euclideanAlgo(res, ary[calcIndex])
      calcIndex += 1

  print(res)

aryLength = int(input())
nums = input().split(' ')
changed = [int(a) for a in nums]
changed.sort()
changed.reverse()
commonDivisor(changed)


#18
#最小公倍数
import math

def euclideanAlgo(a,b):
  if b == 0:
    return a

  s = a % b
  return euclideanAlgo(b, s)

def leastCommonMultiple(a, b):
  return (a / euclideanAlgo(a, b)) * b

calcIndex = 0
def commonDivisor(ary):
  global calcIndex
  res = 0

  for i in range(aryLength - 1):
    if i == 0:
      res = leastCommonMultiple(ary[0], ary[1])
      calcIndex = 2
    else:
      res = leastCommonMultiple(res, ary[calcIndex])
      calcIndex += 1

  print(math.ceil(res))


aryLength = int(input())
nums = input().split(' ')
changed = [int(a) for a in nums]
changed.sort()
changed.reverse()
commonDivisor(changed)

#18
# 組み合わせ
aryLength = int(input())
nums = input().split(' ')
changed = [int(a) for a in nums]
a = list(filter(lambda x: x == 100, changed))
b = list(filter(lambda x: x == 200, changed))
c = list(filter(lambda x: x == 300, changed))
d = list(filter(lambda x: x == 400, changed))

print(len(a)*len(d) + len(c)*len(b))

#19
import math

aryLength = int(input())
nums = input().split(' ')
changed = [int(a) for a in nums]
a = list(filter(lambda x: x == 1, changed))
b = list(filter(lambda x: x == 2, changed))
c = list(filter(lambda x: x == 3, changed))

case = (len(a)*(len(a)-1))/2 + (len(b)*(len(b)-1))/2 + (len(c)*(len(c)-1))/2

print(math.floor(case))


#20
aryLength = int(input())
nums = input().split(' ')
changed = [int(a) for a in nums]

total = 0
for a in range(len(changed)):
  for b in range(a,):
    for c in range(b,):
      for d in range(c,):
        for e in range(d,):
          if (changed[a] + changed[b] + changed[c] + changed[d] + changed[e]) == 1000:
            total += 1

print(total)

#21
import math

a, b = input().split(' ')

numerator = 1
for i in range(int(a) - int(b) + 1, int(a) + 1):
  numerator *= i

denominator = 1
for s in range(0, int(b)):
  denominator *= (s + 1)

print(math.floor(numerator / denominator))

#22
# ちょっとわかんないのでパス

#23
# 期待値
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def expected(ary):
  total = 0
  for i in ary:
    total += i

  return total / len(ary)

print(expected(A) + expected(B))

#24
N = int(input())

def expected():
  total = 0
  for _ in range(N):
    ary = list(map(int, input().split()))
    total += ary[1] / ary[0]

  return total

print(expected())

#25
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def expected(a, b):
  total = 0
  for i in range(N):
    total += (a[i] / 3) + ((b[i] * 2) / 3)

  return total

print(expected(A, B))

#26
N = int(input())

def expected(n):
  total = 0
  for i in range(1, N+1):
    total += 1*N / i

  return total

print(expected(N))