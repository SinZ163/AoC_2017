import sys

def main(code):
    sum = 0
    for i,char in enumerate(code):
        if code[(i + 1) % len(code)] == char:
            sum += int(char)
    print(sum)

if __name__ == "__main__":
    main(sys.argv[1])