from util import read_ints


def calc(ints, rounds):
    pop = {i: 0 for i in range(9)}

    for i in ints:
        pop[i] += 1

    for i in range(rounds):
        zeros = pop[0]

        for k in range(len(pop) - 1):
            pop[k] = pop[k + 1]
        pop[8] = zeros
        pop[6] += zeros

    return sum(pop.values())


def one(ints):
    return calc(ints, 80)


def two(ints):
    return calc(ints, 256)


if __name__ == "__main__":
    i = read_ints("input-6.txt")
    print("one: {}".format(one(i)))
    print("two: {}".format(two(i)))
