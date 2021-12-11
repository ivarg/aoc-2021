from itertools import product


class grid(object):
    g = dict()

    def __init__(self, lines):
        intlines = [list(map(int, list(ln))) for ln in lines]

        for i, line in enumerate(intlines):
            self.g[i] = line
        self.max_i = len(self.g.keys())
        self.max_j = len(self.g[0])

    def neighbors(self, pt, diagonals=True):
        i, j = pt[0], pt[1]
        cands = list(product([i - 1, i, i + 1], [j - 1, j, j + 1]))
        cands = [c for c in cands if not (c[0] == i and c[1] == j)]

        if not diagonals:
            cands = [c for c in cands if (c[0] == i or c[1] == j)]

        cands = [
            c for c in cands if c[0] >= 0 and c[1] >= 0 and c[0] < self.max_i and c[1] < self.max_j
        ]

        return cands

    def get(self, pt):
        return self.g[pt[0]][pt[1]]

    def set(self, pt, v):
        self.g[pt[0]][pt[1]] = v

    def enumerate(self):
        for i, line in self.g.items():
            for j, v in enumerate(line):
                yield ((i, j), v)

    def print(self):
        [print("".join([str(c) for c in ln])) for ln in self.g.values()]
        print()

    def map_all(self, fn):
        self.g = {i: list(map(fn, self.g[i])) for i in self.g.keys()}

    def map_row(self, fn, row):
        self.g[row] = list(map(fn, self.g[row]))

    def map_col(self, fn, col):
        self.g = {i: fn(self.g[i][col]) for i in self.g.keys()}
