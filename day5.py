def main():
    database = []
    newDatabase = []
    with open("day5.input", "r") as f:
        for line in f:
            database.append(int(line.strip()))
            newDatabase.append(int(line.strip()))
    i = 0
    part1Count = 0
    part2Count = 0
    while (i < len(database)):
        database[i] += 1
        i += database[i] - 1
        part1Count += 1
    print(f"Part 1: {part1Count}")
    i = 0
    while (i < len(newDatabase)):
        oldValue = newDatabase[i]
        offset = 1
        if newDatabase[i] >= 3:
            #print("Subtracting instead of Increasing")
            offset = -1
        newDatabase[i] += offset
        i += newDatabase[i] - offset
        part2Count += 1
    print(f"Part 2: {part2Count}")

if __name__ == "__main__":
    main()