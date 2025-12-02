import sys


def get_ranges():
    row = sys.stdin.readlines()[0].strip()
    ranges = row.split(",")
    return ranges


def expand_range(string):
    tokens = list(map(int, string.split("-")))
    numbers = list(range(tokens[0], tokens[1] + 1))
    return numbers


def all_numbers():
    all = []
    for range in get_ranges():
        all = all + expand_range(range)
    return all


def valid_number(number):
    st = str(number)
    size = len(st)
    if size % 2 == 1:
        return True
    half_size = size // 2
    valid = st[:half_size] != st[half_size:]
    return valid


sum = sum([num for num in all_numbers() if not valid_number(num)])

print("Sum:", sum)
