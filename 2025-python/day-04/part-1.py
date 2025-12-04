import os

filename = os.path.join(os.path.dirname(__file__), "input.txt")
# filename = os.path.join(os.path.dirname(__file__), "sample.txt")


def get_rows():
    with open(filename) as f:
        return list(map(lambda s: s.strip(), f.readlines()))


def get_grid():
    return list(map(list, get_rows()))


def is_roll(char):
    return char == "@"


def get_item(grid, x, y):
    if x < 0 or y < 0:
        return None
    try:
        return grid[x][y]
    except IndexError:
        pass


def run():
    grid = get_grid()
    sum = 0

    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            items = [
                get_item(grid, i - 1, j - 1),
                get_item(grid, i - 1, j),
                get_item(grid, i - 1, j + 1),
                get_item(grid, i, j - 1),
                char,
                get_item(grid, i, j + 1),
                get_item(grid, i + 1, j - 1),
                get_item(grid, i + 1, j),
                get_item(grid, i + 1, j + 1),
            ]

            if is_roll(char) and len(list(filter(is_roll, items))) < 5:
                sum += 1

    print("Sum:", sum)


run()

# Result: 1486
