import sys

def main(code):
    sum1 = 0
    sum2 = 0
    for i,char in enumerate(code):
        length = len(code)
        if code[(i + 1) % length] == char:
            sum1 += int(char)
        if code[(i + int(length/2)) % length] == char:
            sum2 += int(char)
            
    print(f"Part 1: {sum1}")
    print(f"Part 2: {sum2}")

if __name__ == "__main__":
    main(sys.argv[1])