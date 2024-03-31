# 数字が１つ
# 入力：N
N = int(input())

# 数字が２つ以上で別々に受け取り
# 入力：A,B
A, B = map(int, input().split())

# 文字列が１つ
# 入力：S
S = input()

# リストで受け取り
# 入力：A1, A2, ....An
A = list(map(int, input().split()))


####  セグメント木
#####segfunc#####
def segfunc(x, y):
    return
#################

#####ide_ele#####
ide_ele =
#################

class SegTree:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(logN)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """
    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res

####  尺取り法（区間積）
def mul_list(data):
    result = 1
    for i in data:
        result *= i
    return result


count = float("inf")
start = 0
end = 0
while True:
    if end >= n or start > end:
        break
    if mul_list(numbers[start: end + 1]) >= k:
        if end - start + 1 < count:
            count = end - start + 1
        start += 1
    elif numbers[end] == 0:
        start = end + 1
        end += 1
    else:
        end += 1

####  繰り返し２乗法
####  https://output-zakki.com/fast_pow_calc/
def pow(x, n):
    ans = 1
    while n > 0:
        if n & 1 == 1:
            ans = ans * x
        x =  x * x
        n >>= 1
    return ans

####  素数判定
####  いろいろある：https://qiita.com/ppza53893/items/e0f464340d6f97760cd5
####  エラトステネスの篩が有名だが、数が大きすぎるとメモリを食い過ぎる
####  下記は√N調べれば、素数かどうかは判別できるというのを利用したもの
def sq(N):
    if N < 2:
        return'NO'
    elif N == 2:
        return 'YES'
    elif N % 2 == 0:
        return 'NO'

    i = 3
    while i <= N ** 0.5:
        if N % i == 0:
            return 'NO'
        i += 2
    return 'YES'
    
print(sq(n))

####  最大公約数
####  ユークリッドの互除法：https://qiita.com/Yuya-Shimizu/items/d82bbdf15d31e25cf544
def gcd(a, b):
    r = a % b

    while r != 0:
        a, b = b, r
        r = a % b

    return b

####  グラフ
####  https://qiita.com/ell/items/2a327fe021fb7dafe07a
####  隣接行列
n, m = map(int, input().split())
graph = [[0]*n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1  # 有向グラフなら消す
print(graph)

####  隣接リスト
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)  # 有向グラフなら消す
print(graph)

####  隣接リストから深さ優先探索
n = int(input())

# リストの元となるオブジェクト
graph = {}
for i in range(n):
    graph[i] = set()

# リスト作成
for i in range(n-1):
    a, b = map(int, input().split())

    graph[a - 1].add(b - 1)
    graph[b - 1].add(a - 1)

# スタックの元
stack = [0]

# 訪問済みかどうかを記録する配列
vis = [False] * n
vis[0] = True

print(1)
# スタックが尽きるまで
while len(stack) != 0:
  s = stack.pop()
  for e in graph[s]:
    # 訪問済みならスキップ
    if vis[e]:
      print(s+1)
      continue
    # 未訪問なら該当のポイントを訪問済みにし、スタックに追加
    vis[e] = True
    stack.append(e)
