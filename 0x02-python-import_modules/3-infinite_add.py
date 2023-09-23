#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sum = 0
    size = len(argv)
    for i in range(1, size):
        sum += int(argv[i])
print(sum)
