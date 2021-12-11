from util import read_lines
from grid import grid


def flash(g):
    nflashed = 0
    toflash = {pt for (pt, v) in g.enumerate() if v == 0}
    flashed = set()

    while len(toflash) > 0:
        pt = toflash.pop()
        nflashed += 1

        for n in g.neighbors(pt):
            if n not in toflash.union(flashed):
                g.set(n, (g.get(n) + 1) % 10)

                if g.get(n) == 0:
                    toflash.add(n)
        flashed.add(pt)

    return nflashed


def one(lines):
    g = grid(lines)

    nflashed = 0

    for n in range(100):
        g.map_all(lambda x: (x + 1) % 10)
        nflashed += flash(g)

    return nflashed


def two(lines):
    g = grid(lines)

    rounds = 0

    while True:
        rounds += 1
        nflashed = 0

        g.map_all(lambda x: (x + 1) % 10)
        nflashed += flash(g)

        if nflashed == g.max_i * g.max_j:
            break

    return rounds


if __name__ == "__main__":
    lines = read_lines("input-11.txt")
    print("one: {}".format(one(lines)))
    print("two: {}".format(two(lines)))
