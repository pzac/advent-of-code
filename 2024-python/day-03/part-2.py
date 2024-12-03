import sys
import re

rows = sys.stdin.readlines()
text = "do" + "".join(row.strip() for row in rows) + "don't"
print(text)
total = 0

valid_chunks = list(re.finditer(r'(do[^n](.+?)don\')', text))

print(valid_chunks)
for chunk in valid_chunks:
    valid_tokens = list(re.finditer(r'mul\((\d+),(\d+)\)', chunk.group()))
    for match in valid_tokens:
        print(match.group())
        total += (int(match.group(1)) * int(match.group(2)))


print("Total ", total)
