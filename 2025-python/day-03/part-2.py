import sys


def get_rows():
    return sys.stdin.readlines()


def joltage(row):
    tokens = list(map(int, row.strip()))
    length = len(tokens)
    stack = []
    while len(stack) < 12:
        missing = 12 - len(stack)
        item = max(tokens[0 : len(tokens) - missing + 1])
        stack.append(item)
        tokens = tokens[tokens.index(item) + 1 :]

    return int("".join(map(str, stack)))


sum = sum([joltage(row) for row in get_rows()])
print("Sum:", sum)

# Result: 168575096286051
