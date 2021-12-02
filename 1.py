from util import read_ints


def one(input):
    return sum([1 for i, v in enumerate(input) if v > input[i - 1]])


def two(input):
    windows = [sum(input[i : i + 3]) for i, _ in enumerate(input)]

    return sum([1 for i, v in enumerate(windows) if v > windows[i - 1]])


if __name__ == "__main__":
    i = read_ints("input-1.txt")
    print("one: {}".format(one(i)))
    print("two: {}".format(two(i)))
