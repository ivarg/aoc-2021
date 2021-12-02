from util import read_lines


def one(lines):
    h = sum([int(ln.split()[1]) for ln in lines if ln.startswith("forward")])
    d = sum([int(ln.split()[1]) for ln in lines if ln.startswith("down")])
    u = sum([int(ln.split()[1]) for ln in lines if ln.startswith("up")])

    return h * (d - u)


def two(lines):
    aim, pos, depth = 0, 0, 0

    for ln in lines:
        op = ln.split()[0]
        n = int(ln.split()[1])

        if op == "forward":
            pos += n
            depth += aim * n

        if op == "down":
            aim += n

        if ln.startswith("up"):
            aim -= n

    return pos * depth


if __name__ == "__main__":
    lines = read_lines("input-2.txt")
    print("one: {}".format(one(lines)))
    print("two: {}".format(two(lines)))
