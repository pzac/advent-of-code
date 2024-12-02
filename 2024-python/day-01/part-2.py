import sys
import re

rows = sys.stdin.readlines()
# print(rows)

left = []
right = []

for row in rows:
    a, b = row.split()
    left.append(int(a))
    right.append(int(b))

sum = 0

for i in range(0, len(left)):
    sum += left[i] * len([x for x in right if x == left[i]])

print(sum)
