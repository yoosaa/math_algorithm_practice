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
####  https://zenn.dev/syuya2036/articles/6e77df7083fc4f#%E6%B7%B1%E3%81%95%E5%84%AA%E5%85%88%E6%8E%A2%E7%B4%A2(dfs)
n = int(input())

# リストの元となるオブジェクト
graph = {}
####  nは頂点の数
for i in range(n):
    graph[i] = set()

# リスト作成
####  n - 1は辺の数
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

###  区間和
###  下記はｎ個のデータ中のk個の区間の和における最大値とその最初のindexを求めるもの
n, k = map(int, input().split())
data = list(map(int, input().split()))

ave = [None] * (n - k + 1)
ave[0] = sum(data[:k])

for i in range(1, n - k + 1):
    ave[i] = ave[i - 1] - data[i - 1] + data[i - 1 + k]

m = max(ave)

print(ave.count(m), ave.index(m) + 1)

### 別解（スライディングウィンドウ法にのっとる）
n, k = map(int, input().split())
visitors = list(map(int, input().split()))

def campaign_period(visitors, k):
    n = len(visitors)
    sums = [None]
    max_sum = sum(visitors[:k])
    sums[0] = sum(visitors[:k])

    for i in range(k, n):
        sums.append(max_sum - visitors[i - k] + visitors[i])
        max_sum = max_sum - visitors[i - k] + visitors[i]
        
    mx = max(sums);

    print(sums.count(mx), sums.index(mx) + 1)
    
campaign_period(visitors, k);

####  リスト（線形）
M = int(input())
data = [None] * M
pointer = [None] * M
head = 0

def add_list(d):
  n = -1
  for i in range(M):
    if data[i] == None:
      n = i
      break
    
  if n == -1:
    return False
    
  for i in range(M):
    if data[i] != None and pointer[i] == None:
      pointer[i] = n
      break
    
  data[n] = d
  pointer[n] = None
  
  return True
  
def show_list():
  p = head
  while True:
    print(data[p])
    if pointer[p] == None:
      break
    p = pointer[p]
    
for i in range(M):
  add_list(int(input()))

show_list()

####  片方向リスト
####  https://yottagin.com/?p=2364# coding: utf-8
# Your code here!
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
class Node():
    #  それぞれのノードはデータと次のノードへのリンクを持つ。
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    # データを設定する。
    def set_data(self, data):
        self.data = data
    # データを取得する。
    def get_data(self):
        return self.data
    # 次のノードを設定する。
    def set_next(self, next):
        self.next = next
    # 次のノードを取得する。
    def get_next(self):
        return self.next

class LinkedList():
    # リストの先頭
    def __init__(self):
        self.head = None
        self.length = 0
    def list_length(self):
        temp = self.head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.get_next()
        return count
    # データの出力
    def print_linked_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
    # 先頭にノードを挿入する。
    def insert_at_start(self, data):
        length = self.list_length()
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node
        self.length = length + 1
    # 最後にノードを挿入する。
    def insert_at_end(self, data):
        length = self.list_length()
        new_node = Node(data)
        temp = self.head
        # 最後のノードまで移動する。
        while temp.get_next() is not None:  
            temp = temp.get_next()
        temp.next = new_node
        self.length = length  + 1
    # ある場所にノードを挿入する。
    def insert_position(self, position, data):
        if position < 0 or position > self.length:
            raise ValueError
        else:
            if position == 0:
                self.insert_at_start(data)
            else:
                if position == self.length:
                    self.insert_at_end(data)
                else:
                    length = self.list_length()
                    new_node = Node(data)
                    count = 0
                    temp = self.head
                    while count < position -1:
                        count += 1
                        temp = temp.get_next()
                    new_node.set_next(temp.get_next())
                    temp.set_next(new_node)
                    self.length = length + 1
    # 指定の位置のデータを削除する
    def delete_position(self, position):
        position -= 1
        if position < 0 or position > self.length:
            raise ValueError
        else:
            length = self.list_length()
            temp = self.head
            if position == 0:
                self.head = temp.get_next()
                temp = None
            else:
              count = 0
              prev = None
              while count < position:
                if temp is None:
                  return
                prev = temp
                temp = temp.get_next()
                count += 1
              prev.next = temp.get_next()
            self.length = length - 1
            return
    # データに基づきノードを削除する。
    def delete(self, data):
        length = self.list_length()
        temp = self.head
        # 削除するノードが先頭の場合
        if (temp.next is not None):
            if(temp.data == data):
                self.head = temp.get_next()
                temp = None
                self.length = length - 1
                return
            else:
                #  ノードを検索する。
                while temp.next is not None:
                    if temp.data == data:
                        break
                    # 現在のノードを一つ前のノードとして保存し、次に進む。
                    prev = temp          
                    temp = temp.get_next()
                # ノードが見つからなかった場合。
                if temp is None:
                    return
                
                self.length = length - 1
                prev.next = temp.get_next()
                return
    # データの検索
    def search(self, node, data):
        if node is None:
            return False
        if node.data == data:
            return True
        return self.search(node.get_next(), data)
        
list = LinkedList()

L, D = map(int, input().split())
for l in range(L):
    inp = int(input())
    if l == 0:
        list.insert_at_start(inp)
    else:
        list.insert_position(l, inp)
        
list.delete_position(D)
list.print_linked_list()
