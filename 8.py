from util import read_lines
from collections import defaultdict

nums = {
    "abcefg": "0",
    "cf": "1",
    "acdeg": "2",
    "acdfg": "3",
    "bcdf": "4",
    "abdfg": "5",
    "abdefg": "6",
    "acf": "7",
    "abcdefg": "8",
    "abcdfg": "9",
}


def invert(d):
    return {v: k for k, v in d.items()}


def decode(pair):
    code, out = pair
    key, rkey = {}, {}

    two = set([c for word in code for c in word if len(word) == 2])  # 1
    three = set([c for word in code for c in word if len(word) == 3])  # 7
    four = set([c for word in code for c in word if len(word) == 4])  # 4
    fives = [set(list(word)) for word in code if len(word) == 5]  # 2,3,5
    sixes = [set(list(word)) for word in code if len(word) == 6]  # 0,6,9
    seven = set([c for word in code for c in word if len(word) == 7])  # 8

    # difference of three (7) and two (1) will give 'a'
    rkey[set.difference(three, two).pop()] = "a"

    # intersection of fives (2,3,5) will give {'a','d','g'}
    # intersection of {'a','d','g'} and four (4) will give {'d'}
    rkey[set.intersection(*fives, four).pop()] = "d"

    # intersection of sixes will give {'a','b','f','g'}
    # intersection of {'a','b','f','g'} and two (1) will give {'f'}
    rkey[set.intersection(*sixes, two).pop()] = "f"

    # difference of two (1), and code for 'f' will give 'c'
    key = invert(rkey)
    rkey[set.difference(two, set(key["f"])).pop()] = "c"

    # difference of four and codes for {'c','d','f'} will give {'b'}
    key = invert(rkey)
    rkey[set.difference(four, set([key["c"], key["d"], key["f"]])).pop()] = "b"

    # difference of {intersection of fives} and {'a','d'} will give {'g'}
    key = invert(rkey)
    rkey[set.difference(set.intersection(*fives), set([key["a"], key["d"]])).pop()] = "g"

    # difference of seven and codes for {'a','b','c','d','f','g'} will give {'e'}
    key = invert(rkey)
    rkey[set.difference(seven, set(key.values())).pop()] = "e"

    res = int("".join([nums["".join(sorted(list(map(lambda k: rkey[k], list(d)))))] for d in out]))

    return res


def one(lines):
    outs = [ln.split("|")[1].strip().split() for ln in lines]

    return sum([1 for out in outs for s in out if len(s) in [2, 4, 3, 7]])


def two(lines):
    pairs = [(ln.split("|")[0].strip().split(), ln.split("|")[1].strip().split()) for ln in lines]

    return sum(list(map(decode, pairs)))


if __name__ == "__main__":
    lines = read_lines("input-8.txt")
    print("one: {}".format(one(lines)))
    print("two: {}".format(two(lines)))
