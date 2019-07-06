from sys import stdout
from bisect import bisect_left as binl
from copy import copy, deepcopy
from collections import defaultdict
 
 
mod = 1
 
 
def intin():
    input_tuple = input().split()
    if len(input_tuple) <= 1:
        return int(input_tuple[0])
    return tuple(map(int, input_tuple))
 
 
def intina():
    return [int(i) for i in input().split()]
 
 
def intinl(count):
    return [intin() for _ in range(count)]
 
 
def modadd(x, y):
    global mod
    return (x + y) % mod
 
 
def modmlt(x, y):
    global mod
    return (x * y) % mod
 
 
def lcm(x, y):
    while y != 0:
        z = x % y
        x = y
        y = z
    return x
 
 
def combination(x, y):
    assert(x >= y)
 
    if y > x // 2:
        y = x - y
 
    ret = 1
 
    for i in range(0, y):
        j = x - i
        i = i + 1
 
        ret = ret * j
        ret = ret // i
 
    return ret
 
 
def get_divisors(x):
    retlist = []
    for i in range(1, int(x**0.5) + 3):
        if x % i == 0:
            retlist.append(i)
            retlist.append(x // i)
    return retlist
 
 
def get_factors(x):
    retlist = []
    for i in range(2, int(x**0.5) + 3):
        while x % i == 0:
            retlist.append(i)
            x = x // i
    retlist.append(x)
    return retlist
 
 
def make_linklist(xylist):
    linklist = {}
    for a, b in xylist:
        linklist.setdefault(a, [])
        linklist.setdefault(b, [])
        linklist[a].append(b)
        linklist[b].append(a)
    return linklist
 
 
def calc_longest_distance(linklist, v=1):
    distance_list = {}
    distance_count = 0
    distance = 0
    vlist_previous = []
    vlist = [v]
    nodecount = len(linklist)
 
    while distance_count < nodecount:
        vlist_next = []
        for v in vlist:
            distance_list[v] = distance
            distance_count += 1
            vlist_next.extend(linklist[v])
        distance += 1
        vlist_to_del = vlist_previous
        vlist_previous = vlist
        vlist = list(set(vlist_next) - set(vlist_to_del))
 
    max_distance = -1
    max_v = None
    for v, distance in distance_list.items():
        if distance > max_distance:
            max_distance = distance
            max_v = v
 
    return (max_distance, max_v)
 
 
def calc_tree_diameter(linklist, v=1):
    _, u = calc_longest_distance(linklist, v)
    distance, _ = calc_longest_distance(linklist, u)
    return distance
 
 
###############################################################################
 
 
def calc_bitmap(i):
    ret = []
    for j in range(10):
        ret.append((i>>j) & 1)
    return ret
 
 
def completes(pclist, bitmap):
    count = 0
    score = 0
    for i, bit in enumerate(bitmap):
        if bit:
            count += pclist[i][0]
            score += ((i+1)*100) * pclist[i][0]
            score += pclist[i][1]
    return count, score
 
 
def not_completes(pclist, bitmap, score):
    count = 0
    lbitmap = []
    for i, bit in enumerate(bitmap):
        if not bit:
            lbitmap.append(i)
    if score <= 0:
        return count
    for i in reversed(lbitmap):
        if score <= 0:
            return count
        if pclist[i][0] > 1:
            if score - ((i+1)*100) * (pclist[i][0] - 1) <= 0:
                if score % ((i+1)*100):
                    count += score // ((i+1)*100) + 1
                else:
                    count += score // ((i+1)*100)
                return count
            count += pclist[i][0] - 1
            score -= (pclist[i][0] - 1) * ((i+1)*100)
    return float('inf')
 
 
def main():
    d, g = intin()
    pclist = intinl(d)
 
    while len(pclist) < 10:
        pclist.append((0, 0))
    min_count = float('inf')
 
    for i in range(2**10):
        bitmap = calc_bitmap(i)
        ccount, score = completes(pclist, bitmap)
        ncount = not_completes(pclist, bitmap, g - score)
        min_count = min(min_count, ccount + ncount)
 
    print(min_count)
 
 
if __name__ == '__main__':
    main()
###############################################################################

from sys import stdout
from bisect import bisect_left as binl
from copy import copy, deepcopy
from collections import defaultdict


mod = 1


def intin():
    input_tuple = input().split()
    if len(input_tuple) <= 1:
        return int(input_tuple[0])
    return tuple(map(int, input_tuple))


def intina():
    return [int(i) for i in input().split()]


def intinl(count):
    return [intin() for _ in range(count)]


def modadd(x, y):
    global mod
    return (x + y) % mod


def modmlt(x, y):
    global mod
    return (x * y) % mod


def lcm(x, y):
    while y != 0:
        z = x % y
        x = y
        y = z
    return x


def combination(x, y):
    assert(x >= y)

    if y > x // 2:
        y = x - y

    ret = 1

    for i in range(0, y):
        j = x - i
        i = i + 1

        ret = ret * j
        ret = ret // i

    return ret


def get_divisors(x):
    retlist = []
    for i in range(1, int(x**0.5) + 3):
        if x % i == 0:
            retlist.append(i)
            retlist.append(x // i)
    return retlist


def get_factors(x):
    retlist = []
    for i in range(2, int(x**0.5) + 3):
        while x % i == 0:
            retlist.append(i)
            x = x // i
    retlist.append(x)
    return retlist


def make_linklist(xylist):
    linklist = {}
    for a, b in xylist:
        linklist.setdefault(a, [])
        linklist.setdefault(b, [])
        linklist[a].append(b)
        linklist[b].append(a)
    return linklist


def calc_longest_distance(linklist, v=1):
    distance_list = {}
    distance_count = 0
    distance = 0
    vlist_previous = []
    vlist = [v]
    nodecount = len(linklist)

    while distance_count < nodecount:
        vlist_next = []
        for v in vlist:
            distance_list[v] = distance
            distance_count += 1
            vlist_next.extend(linklist[v])
        distance += 1
        vlist_to_del = vlist_previous
        vlist_previous = vlist
        vlist = list(set(vlist_next) - set(vlist_to_del))

    max_distance = -1
    max_v = None
    for v, distance in distance_list.items():
        if distance > max_distance:
            max_distance = distance
            max_v = v

    return (max_distance, max_v)


def calc_tree_diameter(linklist, v=1):
    _, u = calc_longest_distance(linklist, v)
    distance, _ = calc_longest_distance(linklist, u)
    return distance


###############################################################################


def calc_bitmap(i):
    ret = []
    for j in range(10):
        ret.append((i>>j) & 1)
    return ret


def completes(pclist, bitmap):
    count = 0
    score = 0
    for i, bit in enumerate(bitmap):
        if bit:
            count += pclist[i][0]
            score += ((i+1)*100) * pclist[i][0]
            score += pclist[i][1]
    return count, score


def not_completes(pclist, bitmap, score):
    count = 0
    lbitmap = []
    for i, bit in enumerate(bitmap):
        if not bit:
            lbitmap.append(i)
    if score <= 0:
        return count
    for i in reversed(lbitmap):
        if score <= 0:
            return count
        if pclist[i][0] > 1:
            if score - ((i+1)*100) * (pclist[i][0] - 1) <= 0:
                if score % ((i+1)*100):
                    count += score // ((i+1)*100) + 1
                else:
                    count += score // ((i+1)*100)
                return count
            count += pclist[i][0] - 1
            score -= (pclist[i][0] - 1) * ((i+1)*100)
    return float('inf')


def main():
    d, g = intin()
    pclist = intinl(d)

    while len(pclist) < 10:
        pclist.append((0, 0))
    min_count = float('inf')

    for i in range(2**10):
        bitmap = calc_bitmap(i)
        ccount, score = completes(pclist, bitmap)
        ncount = not_completes(pclist, bitmap, g - score)
        min_count = min(min_count, ccount + ncount)

    print(min_count)


if __name__ == '__main__':
    main()

