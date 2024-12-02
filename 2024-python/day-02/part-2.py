import sys

rows = sys.stdin.readlines()

def all_increasing(items):
    return sorted(items) == items

def all_decreasing(items):
    return sorted(items) == items[::-1]

def valid_steps(items):
    curr = items[0]
    for t in items[1:]:
        val = abs(t - curr)
        if val < 1 or val > 3:
            return False
        curr = t
    return True


def is_good(items):
    if not valid_steps(items):
        return False
    if not (all_increasing(items) or all_decreasing(items)):
        return False
    return True

def can_be_good(items):
    if is_good(items):
        return True
    for i in range(len(items)):
        copy = items.copy()
        copy.pop(i)
        if is_good(copy):
            return True
    return False

safe = 0
for row in rows:
    tokens = [int(x) for x in row.split()]

    if can_be_good(tokens):
        safe += 1

print("Total: ", safe)
