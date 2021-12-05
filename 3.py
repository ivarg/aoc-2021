from util import read_lines


def one(lines):
    line_length = len(lines)
    gamma_str, eps_str = [], []

    for pos in range(len(lines[0]) - 1):
        sm = 0

        for ln in lines:
            sm += int(ln[pos])

        gamma_str.append("1" if sm > line_length / 2 else "0")
        eps_str.append("0" if sm > line_length / 2 else "1")

    gamma = int("".join(gamma_str), 2)
    eps = int("".join(eps_str), 2)

    return eps * gamma


def two(lines):
    return co2(lines) * oxy(lines)


def co2(lines):
    line_length = len(lines[0])

    for pos in range(line_length):
        sm = 0

        for ln in lines:
            sm += int(ln[pos])

        co2_criteria = 0 if sm >= len(lines) / 2 else 1
        lines = [ln for ln in lines if int(ln[pos]) == co2_criteria]

        if len(lines) < 2:
            break

    return int(lines[0], 2)


def oxy(lines):
    line_length = len(lines[0])

    for pos in range(line_length):
        sm = 0

        for ln in lines:
            sm += int(ln[pos])

        oxy_criteria = 1 if sm >= len(lines) / 2 else 0
        lines = [ln for ln in lines if int(ln[pos]) == oxy_criteria]

        if len(lines) < 2:
            break

    return int(lines[0], 2)


if __name__ == "__main__":
    lines = read_lines("input-3.txt")
    print("one: {}".format(one(lines)))
    print("two: {}".format(two(lines)))
