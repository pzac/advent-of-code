import sys

rows = sys.stdin.readlines()

current = 50
num_zeros = 0

print(f"Position: {current}")

for row in rows:
    row = row.strip()
    dir = row[0]
    num = int(row[1:])

    if dir == "R":
        current += num
    else:
        current -= num

    mod = current % 100

    if mod == 0:
        num_zeros += 1

    print(f"Row: {row} -> {mod} ({current})")
    print(f"Num zeros: {num_zeros}")
