import sys


def get_rows():
    return sys.stdin.readlines()


def joltage(row):
    tokens = list(map(int, row.strip()))
    length = len(tokens)
    a = max(tokens[0 : length - 1])
    b = max(tokens[tokens.index(a) + 1 :])
    return 10 * a + b


sum = sum([joltage(row) for row in get_rows()])

print("Sum:", sum)
