def read_ints():
    inpt = []
    with open("input-1.txt", "r") as f:
        inpt = [int(ln) for ln in f.readlines()]

        return inpt
