from util import read_ints
from sys import maxsize


def calc_fuel(ints, cand, cost_fn):
    return sum([cost_fn(cand, crab) for crab in ints])


def optimise(ints, cost_fn):
    c_low = maxsize

    for cand in range(min(ints), max(ints)):
        c = calc_fuel(ints, cand, cost_fn)

        if c < c_low:
            c_low = c
        else:
            break

    return c_low


def one(ints):
    return optimise(ints, lambda cand, p_crab: abs(p_crab - cand))


def two(ints):
    return optimise(ints, lambda cand, p_crab: sum(range(abs(p_crab - cand) + 1)))


if __name__ == "__main__":
    i = read_ints("input-7.txt")
    print("one: {}".format(one(i)))
    print("two: {}".format(two(i)))
