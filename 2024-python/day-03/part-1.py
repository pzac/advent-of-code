import sys
import re

rows = sys.stdin.readlines()
print(rows)
total = 0
for row in rows:
    valid_tokens = list(re.finditer(r'mul\((\d+),(\d+)\)', row))
    for match in valid_tokens:
        total += (int(match.group(1)) * int(match.group(2)))


print("Total ", total)
