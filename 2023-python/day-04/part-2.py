import sys
import re

rows = sys.stdin.readlines()





def extract_numbers(data):
  return [int(m.group()) for m in re.finditer(r'\d+', data)]


items = []
for i, row in enumerate(rows):
  _label, data = row.split(":")
  left, right = [extract_numbers(x) for x in data.split("|")]
  matches = [i for i in left if i in right]
  items.append(
    (i+1, left, right, len(matches))
  )

# for item in items:
#   print(item)


todo = [x for x in items]
done = []

while len(todo) > 0:
  item = todo.pop(0)
  matches = item[3]
  # print("todo: ", len(todo), "matches ", matches)
  print("Processing", item)
  print(" Adding", matches, "records")


  for i in range(0, matches):
    current_item_index = item[0] - 1
    index_to_add = current_item_index + i + 1
    if index_to_add < len(items):
      print("Adding item", index_to_add)
      to_add = items[index_to_add]
      todo.append(to_add)
  done.append(item)

print("Total cards:", len(done))

