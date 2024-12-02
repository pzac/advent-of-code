import sys

rows = sys.stdin.readlines()
print(rows)


def all_increasing(list):
    return sorted(list) == list

def all_decreasing(list):
    return sorted(list) == list[::-1]

def valid_steps(list):
    good = True
    curr = list[0]
    for t in list[1:]:
        val = abs(t - curr)
        if val < 1 or val > 3:
            good = False
        curr = t
    return good


def is_good(list):
    if not valid_steps(tokens):
        return False
    if not (all_increasing(tokens) or all_decreasing(tokens)):
        return False
    return True

safe = 0
for row in rows:
    tokens = [int(x) for x in row.split()]
    if is_good(tokens):
        safe += 1

print(safe)
