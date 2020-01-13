import enum

Color = enum.Enum("Color", "R B Error") # R:赤, B:黒, Error:debug 用

class Node: # ノードの型
    def __init__(self, color, key, x):
        self.color = color # そのノードの色
        self.key   = key   # そのノードのキー
        self.value = x     # そのノードの値
        self.lst   = None  # 左部分木
        self.rst   = None  # 右部分木

# ノードが赤かチェックする
def isR(node): return node is not None and node.color == Color.R

# ノードが黒かチェックする
def isB(node): return node is not None and node.color == Color.B

def rotateL(v): # ２分探索木 v の左回転。回転した木を返す
    u = v.rst; t2 = u.lst
    u.lst = v; v.rst = t2
    return u
def rotateR(u): # ２分探索木 u の右回転。回転した木を返す
    v = u.lst; t2 = v.rst
    v.rst = u; u.lst = t2
    return v
def rotateLR(t): # ２分探索木 t の二重回転(左回転 -> 右回転)。回転した木を返す
    t.lst = rotateL(t.lst)
    return rotateR(t)
def rotateRL(t): # ２分探索木 t の二重回転(右回転 -> 左回転)。回転した木を返す
    t.rst = rotateR(t.rst)
    return rotateL(t)

class RBMap:
    def __init__(self):
        self.root   = None  # 赤黒木の根。Node 型
        self.change = False # 修正が必要かを示すフラグ(True:必要, False:不要)
        self.lmax   = None  # 左部分木のキーの最大値
        self.value  = None  # lmax に対応する値

    # エントリー(key, x のペア)を挿入する
    def insert(self, key, x):
        self.root = self.insert_sub(self.root, key, x)
        self.root.color = Color.B

    def insert_sub(self, t, key, x):
        if t is None:
            self.change = True
            return Node(Color.R, key, x)
        elif key < t.key:
            t.lst = self.insert_sub(t.lst, key, x)
            return self.balance(t)
        elif key > t.key:
            t.rst = self.insert_sub(t.rst, key, x)
            return self.balance(t)
        else:
            self.change = False
            t.value = x
            return t

    # エントリー挿入に伴う赤黒木の修正(パターンマッチ)
    def balance(self, t):
        if not self.change:
            return t
        elif not isB(t): # 根が黒でないなら何もしない。change フラグも変えない
            return t
        elif isR(t.lst) and isR(t.lst.lst):
            t = rotateR(t)
            t.lst.color = Color.B
        elif isR(t.lst) and isR(t.lst.rst):
            t = rotateLR(t)
            t.lst.color = Color.B
        elif isR(t.rst) and isR(t.rst.lst):
            t = rotateRL(t)
            t.rst.color = Color.B
        elif isR(t.rst) and isR(t.rst.rst):
            t = rotateL(t)
            t.rst.color = Color.B
        else:
            self.change = False
        return t

    # key で指すエントリー(ノード)を削除する
    def delete(self, key):
        self.root = self.delete_sub(self.root, key)
        if self.root is not None: self.root.color = Color.B

    def delete_sub(self, t, key):
        if t is None:
            self.change = False
            return None
        elif key < t.key:
            t.lst = self.delete_sub(t.lst, key)
            return self.balanceL(t)
        elif key > t.key:
            t.rst = self.delete_sub(t.rst, key)
            return self.balanceR(t)
        else:
            if t.lst is None:
                if t.color == Color.R:
                    self.change = False
                else:
                    self.change = True
                return t.rst # 右部分木を昇格させる
            else:
                t.lst = self.delete_max(t.lst) # 左部分木の最大値を削除する
                t.key = self.lmax # 左部分木の削除した最大値で置き換える
                t.value = self.value
                return self.balanceL(t)

    # 部分木 t の最大値のノードを削除する
    # 戻り値は削除により修正された部分木
    # 削除した最大値を lmax に保存する
    def delete_max(self, t):
        if t.rst is not None:
            t.rst = self.delete_max(t.rst)
            return self.balanceR(t)
        else:
            self.lmax = t.key # 部分木のキーの最大値を保存
            self.value = t.value
            if t.color == Color.R:
                self.change = False
            else:
                self.change = True
            return t.lst # 左部分木を昇格させる

    # 左部分木のノード削除に伴う赤黒木の修正(パターンマッチ)
    # 戻り値は修正された木
    def balanceL(self, t):
        if not self.change: # 修正なしと赤ノードを削除した場合はここになる
            return t        # つまり、以下は黒ノードを削除した場合のみ
        elif isB(t.rst) and isR(t.rst.lst):
            rb = t.color
            t = rotateRL(t)
            t.color = rb
            t.lst.color = Color.B
            self.change = False
        elif isB(t.rst) and isR(t.rst.rst):
            rb = t.color
            t = rotateL(t)
            t.color = rb
            t.lst.color = Color.B
            t.rst.color = Color.B
            self.change = False
        elif isB(t.rst):
            rb = t.color
            t.color = Color.B
            t.rst.color = Color.R
            self.change = (rb == Color.B)
        elif isR(t.rst):
            t = rotateL(t)
            t.color = Color.B
            t.lst.color = Color.R
            t.lst = self.balanceL(t.lst)
            self.change = False
        else: # 黒ノード削除の場合、ここはありえない
            print("(L) This program is buggy")
            sys.exit(1)
        return t;

    # 右部分木のノード削除に伴う赤黒木の修正(パターンマッチ)
    # 戻り値は修正された木
    def balanceR(self, t):
        if not self.change: # 修正なしと赤ノードを削除した場合はここになる
            return t        # つまり、以下は黒ノードを削除した場合のみ
        elif isB(t.lst) and isR(t.lst.rst):
            rb = t.color
            t = rotateLR(t)
            t.color = rb
            t.rst.color = Color.B
            self.change = False
        elif isB(t.lst) and isR(t.lst.lst):
            rb = t.color
            t = rotateR(t)
            t.color = rb
            t.lst.color = Color.B
            t.rst.color = Color.B
            self.change = False
        elif isB(t.lst):
            rb = t.color
            t.color = Color.B
            t.lst.color = Color.R
            self.change = (rb == Color.B)
        elif isR(t.lst):
            t = rotateR(t)
            t.color = Color.B
            t.rst.color = Color.R
            t.rst = self.balanceR(t.rst)
            self.change = False
        else: # 黒ノード削除の場合、ここはありえない
            print("(R) This program is buggy")
            sys.exit(1)
        return t;

    # キーの検索。ヒットすれば True、しなければ False
    def member(self, key):
        t = self.root
        while t is not None:
            if key < t.key:
                t = t.lst
            elif key > t.key:
                t = t.rst
            else:
                return True
        return False

    # キーから値を得る。キーがヒットしない場合は None を返す
    def lookup(self, key):
        t = self.root
        while t is not None:
            if key < t.key:
                t = t.lst
            elif key > t.key:
                t = t.rst
            else:
                return t.value
        return None

    # マップが空なら True、空でないなら False
    def isEmpty(self): return self.root is None

    # マップを空にする
    def clear(self): self.root = None

    # キーのリスト
    def keys(self): return keys_sub(self.root)

    # 値のリスト
    def values(self): return values_sub(self.root)

    # エントリーのリスト
    def items(self): return items_sub(self.root)

    # マップのサイズ
    def size(self): return len(self.keys())

    def __contains__(self, key): self.member(key)
    def __getitem__(self, key): return self.lookup(key)
    def __setitem__(self, key, x): return self.insert(key, x)
    def __delitem__(self, key): self.delete(key)
    def __bool__(self): return not self.isEmpty()
    def __len__(self): return self.size()
    def __iter__(self): return iter(self.keys())

    # 赤黒木をグラフ文字列に変換する
    def __str__(self): return toGraph("", "", self.root).rstrip()

    # 赤黒木のバランスが取れているか確認する
    def balanced(self): return blackHeight(self.root) >= 0

    # 赤黒木の配色が正しいか確認する
    def colorValid(self): return colorChain(self.root) == Color.B

    # ２分探索木になっているか確認する
    def bstValid(self): return bstValid(self.root)

def keys_sub(t):
    if t is None: return []
    return keys_sub(t.lst) + [t.key] + keys_sub(t.rst)

def values_sub(t):
    if t is None: return []
    return values_sub(t.lst) + [t.value] + values_sub(t.rst)

def items_sub(t):
    if t is None: return []
    return items_sub(t.lst) + [(t.key, t.value)] + items_sub(t.rst)

def toGraph(head, bar, t):
    graph = ""
    if t != None:
        graph += toGraph(head + "    ", "／", t.rst)
        node = "R" if t.color == Color.R else "B"
        node += ":" + str(t.key) + ":" + str(t.value)
        graph += head + bar + node + "\n"
        graph += toGraph(head + "    ", "＼", t.lst)
    return graph

def blackHeight(t):
    if t is None: return 0
    nl = blackHeight(t.lst)
    nr = blackHeight(t.rst)
    if nl < 0 or nr < 0 or nl != nr: return -1
    if t.color == Color.B:
        return nl + 1
    else:
        return nl

def colorChain(t):
    if t is None: return Color.B
    p = t.color
    cl = colorChain(t.lst)
    cr = colorChain(t.rst)
    if cl == Color.Error or cr == Color.Error:
        return Color.Error
    elif p == Color.B:
        return p
    elif p == Color.R and cl == Color.B and cr == Color.B:
        return p
    else:
        return Color.Error

def bstValid(t):
    if t is None: return True
    flag = small(t.key, t.lst) and large(t.key, t.rst)
    return flag and bstValid(t.lst) and bstValid(t.rst)
def small(key, t):
    if t is None: return True
    return t.key < key and small(key, t.lst) and small(key, t.rst)
def large(key, t):
    if t is None: return True
    return t.key > key and large(key, t.lst) and large(key, t.rst)
    
    
if __name__ == '__main__':
    import random
    n = 30
    m = RBMap() # 赤黒木マップを生成
    keys = list(range(n))
    random.shuffle(keys)
    for i, key in enumerate(keys): m[key] = i
    print(m)
    print()
    for key in sorted(keys[:5]):
        print("m[{0:>2}] == {1}".format(key, m[key]))
    print()
    print("size: ", len(m))
    print("keys: ", m.keys())

    N = 100000
    m.clear()
    answer = {}
    insertErrors = 0
    for i in range(N):
        key = random.randrange(N)
        m.insert(key, i)
        answer[key] = i
    for key in answer:
        if m[key] != answer[key]:
            insertErrors += 1
    deleteKeys = random.sample(answer.keys(), len(answer)//2)
    deleteErrors = 0
    for key in deleteKeys: m.delete(key)
    for key in deleteKeys:
        if key in m:
            deleteErrors += 1

    def okng(flag): return "OK" if flag else "NG"
    print()
    print("バランス:  ", okng(m.balanced()))
    print("２分探索木:", okng(m.bstValid()))
    print("配色:      ", okng(m.colorValid()))
    print("挿入:      ", okng(insertErrors == 0))
    print("削除:      ", okng(deleteErrors == 0))
    for key in m: del m[key]
    print("全削除:    ", okng(not m))
