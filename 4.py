from util import read_file


def draw(n, board):
    board = [[-1 if c == n else c for c in line] for line in board]

    return board


def iswin(board):
    for line in board:
        if sum(line) == -5:
            return True

    for i in range(len(board[0])):
        if sum([line[i] for line in board]) == -5:
            return True

    return False


def one(numbers, boards):
    numbers = [int(n) for n in numbers]
    boards = [[[int(c) for c in line.split()] for line in b.split("\n")] for b in boards]

    for n in numbers:
        boards = [draw(n, b) for b in boards]

        for board in boards:
            if iswin(board):
                board = [[0 if c < 0 else c for c in line] for line in board]

                return n * sum([sum(line) for line in board])


def two(numbers, boards):
    numbers = [int(n) for n in numbers]
    boards = [[[int(c) for c in line.split()] for line in b.split("\n")] for b in boards]

    for n in numbers:
        boards = [draw(n, b) for b in boards]
        boards = [b for b in boards if not iswin(b)]

        if len(boards) == 1:
            b = boards[0]

            for n in numbers:
                b = draw(n, b)

                if iswin(b):
                    b = [[0 if c < 0 else c for c in line] for line in b]

                    return n * sum([sum(line) for line in b])


if __name__ == "__main__":
    input = read_file("input-4.txt").strip().split("\n\n")
    print(one(input[0].split(","), input[1:]))
    print(two(input[0].split(","), input[1:]))
