# 8
N=int(input())
a=list(map(int, input().split()))
aSet = set(a)
print(len(aSet))

# 9
x1, y1=map(int, input().split())
x2, y2=map(int, input().split())
x3, y3=map(int, input().split())
if x1 == x2:
    x4 = x3
elif x2 == x3:
    x4 = x1
elif x1 == x3:
    x4 = x2
if y1 == y2:
    y4 = y3
elif y2 == y3:
    y4 = y1
elif y1 == y3:
    y4 = y2
print(x4, y4)

# 10
N=int(input())
mountains = []
for i in range(N):
    S, T = map(str, input().split())
    T = int(T)
    mountains.append([T, S])
mountains.sort(reverse=True)
print(mountains[1][1])