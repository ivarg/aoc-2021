def read_ints(file):
    inpt = []
    with open(file, "r") as f:
        inpt = [int(ln) for ln in f.readlines()]

        return inpt


def read_lines(file):
    inpt = []
    with open(file, "r") as f:
        inpt = [ln for ln in f.readlines()]

        return inpt
