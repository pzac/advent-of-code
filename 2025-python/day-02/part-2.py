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
    for chunk_size in range(1, size):
        chunks = [st[i : i + chunk_size] for i in range(0, size, chunk_size)]
        if len(set(chunks)) == 1:
            return False
    return True


all = all_numbers()

sum = 0
for num in all:
    if not valid_number(num):
        sum += num

print("Sum:", sum)
