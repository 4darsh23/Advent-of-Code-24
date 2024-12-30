import argparse


def read_input(filename):
    requested = []
    patterns = []
    with open(filename, 'r') as file:
        patterns = file.readline().strip().split(", ")
        file.readline()

        for line in file:
            requested.append(line.strip())
    return patterns, requested


def count_patterns(design, patterns, memo={}):
    if design == "":
        return 1
    if design in memo:
        return memo[design]

    total = 0
    for pat in patterns:
        if design.startswith(pat):
            remaining = design[len(pat):]
            total += count_patterns(remaining, patterns, memo)

    memo[design] = total
    return total


def solve(patterns, requested):
    possible = 0
    total_arrangements = 0

    for design in requested:
        ct = count_patterns(design, patterns)
        if ct > 0:
            possible += 1
        total_arrangements += ct

    return possible, total_arrangements


if __name__ == '__main__':
    parser = argparse.ArgumentParser("main.py")
    parser.add_argument("filename", nargs='?',
                        help="input filename", default="input.txt")
    args = parser.parse_args()

    patterns, requested = read_input(args.filename)

    p1, p2 = solve(patterns, requested)
    print(f"\nPart1: {p1}")
    print(f"Part2: {p2}\n")