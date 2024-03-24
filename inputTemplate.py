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
