import sys

rows = sys.stdin.readlines()
print(rows)

left = []
right = []

for row in rows:
    a, b = row.split()
    left.append(int(a))
    right.append(int(b))

left = sorted(left)
right = sorted(right)

sum = 0
for i in range(0, len(left)):
    sum += abs(left[i] - right[i])

print(sum)
