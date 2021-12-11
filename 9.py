import math
from util import read_lines
from grid import grid


def basin(s, g):
    cands = set(g.neighbors(s, diagonals=False))
    visited = set()
    res = set()

    while True:
        if len(cands) == 0:
            break
        c = cands.pop()
        visited.add(c)

        if g.get(c) < 9:
            res.add(c)
            nbrs = set(g.neighbors(c, diagonals=False))
            cands = cands.union(nbrs.difference(visited))

    return res


def sinks(g):
    res = []

    for pt in g.enumerate():
        if len([c for c in g.neighbors(pt[0], diagonals=False) if pt[1] >= g.get(c)]) == 0:
            res.append(pt)

    return res


def one(lines):
    g = grid(lines)

    return sum([p[1] + 1 for p in sinks(g)])


def two(lines):
    g = grid([list(map(int, list(ln))) for ln in lines])
    ss = sinks(g)
    res = sorted([len(basin(s[0], g)) for s in ss])

    return math.prod(res[len(res) - 3 :])


if __name__ == "__main__":
    lines = read_lines("input-9.txt")
    print("one: {}".format(one(lines)))
    print("two: {}".format(two(lines)))
