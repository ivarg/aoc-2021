from util import read_lines

chrs = {"<": ">", "(": ")", "{": "}", "[": "]"}


def count_errors(line):
    stack = []
    errors = []

    for c in line:
        if c in chrs.keys():
            stack.append(c)
        else:
            pop = stack.pop()

            if c != chrs[pop]:
                errors.append(c)

    return errors, stack


def one(lines):
    points = {">": 25137, ")": 3, "}": 1197, "]": 57}
    errors = []

    for line in lines:
        e, _ = count_errors(line)
        errors.extend(e)

    return sum([points[v] for v in errors])


def two(lines):
    points = {">": 4, ")": 1, "}": 3, "]": 2}
    scores = []

    for line in lines:
        errors, stack = count_errors(line)

        if len(errors) > 0:
            continue

        score = 0

        for c in [chrs[c] for c in reversed(stack)]:
            score = (score * 5) + points[c]
        scores.append(score)

    return sorted(scores)[int(len(scores) / 2)]


if __name__ == "__main__":
    lines = read_lines("input-10.txt")
    print("one: {}".format(one(lines)))
    print("two: {}".format(two(lines)))
