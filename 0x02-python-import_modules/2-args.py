#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    size = len(argv) - 1
    if size == 0:
        print(size, "arguments.")
    elif size == 1:
        print(size, "argument:")
    else:
        print(size, "arguments:")
    for i in range(1, size + 1):
        print(i, ": ", argv[i], sep="")
