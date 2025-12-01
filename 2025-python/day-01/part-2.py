import sys

rows = sys.stdin.readlines()

curr = 50
num_zeros = 0

print(f"Position: {curr}")

for row in rows:
    prev = curr
    row = row.strip()
    dir = row[0]
    num = int(row[1:])

    if dir == "R":
        curr += num
    else:
        curr -= num

    curr_mod = curr % 100
    prev_mod = prev % 100

    if dir == "R":
        if abs(curr - prev) > 100:
            num_zeros += abs(curr - prev) // 100
        if (prev_mod > curr_mod and prev_mod != 0) or (curr_mod == 0):
            num_zeros += 1
    else:
        if abs(curr - prev) > 100:
            num_zeros += abs(curr - prev) // 100
        if (prev_mod < curr_mod and prev_mod != 0) or (curr_mod == 0):
            num_zeros += 1

    print(f"Row: {row} -> {curr} ({curr_mod}):{num_zeros}")
