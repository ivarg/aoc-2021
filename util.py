def read_ints(file):
    inpt = []
    with open(file, "r") as f:
        inpt = [int(ln) for ln in f.read().split(",")]

        return inpt


def read_lines(file):
    inpt = []
    with open(file, "r") as f:
        inpt = [ln.strip() for ln in f.readlines()]

        return inpt


def read_file(file):
    with open(file, "r") as f:
        return f.read()
