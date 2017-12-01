import sys

def main(code):
    sum = 0
    skip = len(code)/2
    for i,char in enumerate(code):
        if code[(i + int(skip)) % len(code)] == char:
            sum += int(char)
    print(sum)

if __name__ == "__main__":
    main(sys.argv[1])